"""
Hospital Admission Check Web Application
"""

import sqlite3
from datetime import datetime
from flask import Flask, request, render_template

app = Flask(__name__)

DB_NAME = "hospital.db"


def init_db():
    """Create the admission_checks table if it doesn't already exist."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS admission_checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER NOT NULL,
            temperature REAL NOT NULL,
            severity TEXT NOT NULL,
            ward TEXT NOT NULL,
            priority TEXT NOT NULL,
            charge INTEGER NOT NULL,
            reason TEXT,
            checked_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_check(age, temp, severity, result):
    """Insert one admission-check record into the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO admission_checks
           (age, temperature, severity, ward, priority, charge, reason, checked_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (age, temp, severity, result["ward"], result["priority"],
         result["charge"], result["reason"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()


def triage(age, temp, severity):
    """
    Simple rule-based logic to decide ward, priority, and charges.
    Real hospitals use far more complex protocols - this is a simplified demo.
    """
    reasons = []
    risk_score = 0

    # --- Severity contributes to risk score ---
    if severity == "severe":
        risk_score += 3
    elif severity == "moderate":
        risk_score += 2
    else:
        risk_score += 1

    # --- Fever contributes to risk score ---
    if temp >= 103:
        risk_score += 2
        reasons.append("high fever")
    elif temp >= 100.4:
        risk_score += 1
        reasons.append("mild fever")

    # --- Age group contributes to risk score ---
    if age >= 65 or age <= 5:
        risk_score += 1
        reasons.append("high-risk age group")

    # --- Decide ward/priority from total risk score ---
    if risk_score >= 5:
        ward, priority, css_class, charge = "ICU", "Emergency", "icu", 8000
    elif risk_score >= 3:
        ward, priority, css_class, charge = "General Ward", "Urgent", "general", 2500
    else:
        ward, priority, css_class, charge = "OPD (Outpatient)", "Normal", "opd", 500

    reason_text = ", ".join(reasons) if reasons else "no significant risk factors"

    return {
        "ward": ward,
        "priority": priority,
        "css_class": css_class,
        "charge": charge,
        "reason": reason_text,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    age = temp = severity = None
    result = None
    error = None

    if request.method == "POST":
        severity = request.form.get("severity", "mild")
        try:
            age = int(request.form.get("age"))
            temp = float(request.form.get("temp"))

            if age < 0 or age > 120:
                error = "Please enter a realistic age (0-120)."
            elif temp < 90 or temp > 112:
                error = "Please enter a realistic body temperature in °F."
            else:
                result = triage(age, temp, severity)
                save_check(age, temp, severity, result)

        except (ValueError, TypeError):
            error = "Please enter valid numbers for age and temperature."

    return render_template(
        "main.html",
        age=age, temp=temp, severity=severity,
        result=result, error=error
    )


init_db()  # ensure the table exists as soon as the app starts

if __name__ == "__main__":
    app.run(debug=True)
