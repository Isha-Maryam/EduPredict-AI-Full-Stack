# 🎓 EduPredict AI: Student Performance Analysis System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## 🚀 Overview
**EduPredict AI** is a full-stack Machine Learning application designed to help educators and institutions predict student academic outcomes based on behavioral and historical data. By leveraging a **Random Forest Regressor**, the system provides high-accuracy math score predictions, enabling early intervention for at-risk students.

---

## ✨ Key Features
* **🧠 Intelligent Prediction:** Uses a trained Random Forest model to analyze 7+ key academic metrics.
* **📊 Dynamic Dashboard:** A clean, modern UI built with Bootstrap 5 for seamless user experience.
* **📜 History Tracking:** Integrated SQLite database to store and review past predictions.
* **🛡️ Data Validation:** Robust Django-form handling to ensure data integrity.
* **📱 Responsive Design:** Fully functional on mobile, tablet, and desktop.

---

## 🛠️ Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.x, Django 5.x |
| **Machine Learning** | Scikit-Learn, Pandas, Joblib |
| **Frontend** | HTML5, CSS3 (Inter Font), Bootstrap 5 |
| **Database** | SQLite (Production-ready for small-scale deployment) |

---

## 📂 Project Structure
* `predictor/` - Core Django app containing ML logic.
* `models/` - Pre-trained Random Forest model (`.pkl` file).
* `templates/` - Modern UI components and layouts.
* `static/` - Custom CSS and branding assets.

---

## ⚙️ Installation & Setup
1. **Clone the repository:**
```bash
git clone [https://github.com/Isha-Maryam/Student_performance_project.git](https://github.com//Isha-Maryam/Student_performance_project.git)

```

2. **Setup Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```


3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run Migrations & Server:**
```bash
python manage.py migrate
python manage.py runserver

```
---

## 📈 ML Model Details

The underlying model is a **Random Forest Regressor** trained on features including:

* 📖 Study Hours & Practice Hours
* 🏫 Attendance Rate
* 🎓 Parent Education Level
* 😴 Sleep Patterns
* 📉 Previous Grade Averages

---

## 💼 Business Use Case (Freelance Focus)

This project is built as a **SaaS MVP (Minimum Viable Product)** for educational consultants. It demonstrates the ability to bridge the gap between complex Data Science and user-friendly web applications—a high-value skill in the freelance market.

---

## 📧 Contact & Connect

**Isha Maryam** - ML | Deep Learning | Full-Stack Developer

*Let's build something intelligent together!* [LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/in/isha-maryam-84ab8a327) | [Portfolio](https://www.google.com/search?q=https://isha-maryam-ai-engineer.web.app/)

```

