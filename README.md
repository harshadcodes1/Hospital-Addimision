# 🏥 Hospital Admission Logic Checker

## 📌 About the Project

Hospital Admission Logic Checker is a simple web-based application developed using **Python, Flask, HTML, CSS, and SQLite**.

The application checks basic patient information such as **age, body temperature, and symptom severity** and provides a recommended ward and priority level based on predefined rules.

This project is created for **educational purposes** to demonstrate Python programming, Flask web development, and database connectivity.

## ✨ Features

* Enter patient's age
* Enter body temperature
* Select symptom severity
* Calculate patient risk score
* Recommend appropriate hospital ward
* Display admission priority
* Display estimated bed charges
* Display reasons for the recommendation
* Store admission-check records in SQLite database

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **HTML**
* **CSS**

## 🧠 Admission Logic

The application calculates a risk score based on:

### Symptom Severity

* Mild → 1 point
* Moderate → 2 points
* Severe → 3 points

### Temperature

* 100.4°F or above → additional risk point
* 103°F or above → higher risk score

### Age

* Age 65 or above → additional risk point
* Age 5 or below → additional risk point

### Final Recommendation

| Risk Score | Recommended Ward | Priority  | Estimated Charge |
| ---------- | ---------------- | --------- | ---------------- |
| 5 or more  | ICU              | Emergency | ₹8,000/day       |
| 3–4        | General Ward     | Urgent    | ₹2,500/day       |
| Below 3    | OPD              | Normal    | ₹500/day         |

## 🗄️ Database

The project uses **SQLite** to store admission-check information.

The database stores:

* Patient age
* Temperature
* Symptom severity
* Recommended ward
* Priority
* Estimated charge
* Reason
* Date and time of the check

## 📂 Project Structure

```text
Hospital-Admission-Logic-Checker/
│
├── Main.py
├── hospital.db
├── templates/
│   └── main.html
├── static/
│   └── design.css
└── README.md
```

## ▶️ How to Run the Project

### 1. Install Python

Make sure Python is installed on your computer.

Check using:

```bash
python --version
```

### 2. Install Flask

```bash
pip install flask
```

### 3. Open the Project Folder

Open the project folder in **VS Code** or Command Prompt.

### 4. Run the Application

```bash
python Main.py
```

### 5. Open in Browser

Open:

```text
http://127.0.0.1:5000/
```

## 📚 Learning Outcomes

By developing this project, I learned:

* Python programming
* Flask framework
* HTML and CSS
* SQLite database connectivity
* Form handling
* Rule-based decision making
* Backend and frontend integration
* Data storage using SQLite
* Git and GitHub

## ⚠️ Disclaimer

This project is developed **only for educational purposes**.

The admission recommendations are based on simplified rules and **should not be used for real medical diagnosis or hospital admission decisions**.

## 👨‍💻 Author

**Harshad Jalindar Nikam**

Electronics & Computer Engineering

---

