# 📚 Student Attendance Tracker

A simple Student Attendance Tracker built using **Python and Streamlit**.

The application allows users to add students, mark attendance, view student information, and automatically calculate attendance percentages.

## 🚀 Features

* Add student details
* Store student data using JSON
* Mark student attendance
* Store attendance using JSON
* Automatically calculate attendance percentage
* View attendance reports
* View student list
* Dashboard with attendance statistics
* No traditional database required
* Simple and beginner-friendly Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* JSON
* Git
* GitHub
* Streamlit Community Cloud

## 📁 Project Structure

```text
student-attendance-tracker
│
├── app.py
├── data.py
├── requirements.txt
├── README.md
│
└── data
    ├── students.json
    └── attendance.json
```

## 📊 Attendance Calculation

The application calculates attendance using:

```text
Attendance Percentage =
(Present Classes / Total Classes) × 100
```

### Example

```text
Present Classes = 8
Total Classes = 10

Attendance Percentage =
(8 / 10) × 100

= 80%
```

## ▶️ How to Run Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-attendance-tracker.git
```

### Step 2: Open the project

```bash
cd student-attendance-tracker
```

### Step 3: Install Streamlit

```bash
pip install streamlit
```

### Step 4: Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📝 How to Use

### 1. Add Student

Enter:

* Student ID
* Student Name
* Department
* Year

Click **Add Student**.

### 2. Mark Attendance

Select:

* Student
* Date
* Present or Absent

Click **Save Attendance**.

### 3. Attendance Report

The application automatically displays:

* Total classes
* Present classes
* Absent classes
* Attendance percentage

### 4. Student List

View all registered students and their details.

## 💾 Data Storage

This project does not use MySQL, PostgreSQL, MongoDB, SQLite, or any other traditional database.

All data is stored in:

```text
data/students.json
data/attendance.json
```

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the `student-attendance-tracker` repository.
5. Select the `main` branch.
6. Select `app.py` as the main file.
7. Click **Deploy**.

## 🎯 Project Objective

The objective of this project is to demonstrate:

* Python programming
* Streamlit application development
* Form handling
* JSON file handling
* Data processing
* Attendance calculations
* Git and GitHub
* Cloud deployment

## 👩‍💻 Author

Meghana

## 📌 Project

**Student Attendance Tracker**

Built with Python + Streamlit + JSON.
