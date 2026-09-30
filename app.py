import streamlit as st
from datetime import date

from data import (
    load_students,
    save_students,
    load_attendance,
    save_attendance
)


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Student Attendance Tracker",
    page_icon="📚",
    layout="wide"
)


# -----------------------------
# LOAD DATA
# -----------------------------

students = load_students()
attendance = load_attendance()


# -----------------------------
# TITLE
# -----------------------------

st.title("📚 Student Attendance Tracker")

st.write(
    "A simple attendance management system using Streamlit and JSON files."
)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Choose an option",
    [
        "Dashboard",
        "Add Student",
        "Mark Attendance",
        "Attendance Report",
        "Student List"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if menu == "Dashboard":

    st.header("🏠 Dashboard")

    total_students = len(students)

    total_classes = len(attendance)

    present_count = sum(
        1 for record in attendance
        if record["status"] == "Present"
    )

    absent_count = sum(
        1 for record in attendance
        if record["status"] == "Absent"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Students",
            total_students
        )

    with col2:
        st.metric(
            "Attendance Records",
            total_classes
        )

    with col3:
        st.metric(
            "Present",
            present_count
        )

    with col4:
        st.metric(
            "Absent",
            absent_count
        )

    st.divider()

    if total_classes > 0:

        overall_percentage = (
            present_count / total_classes
        ) * 100

        st.subheader("Overall Attendance")

        st.progress(
            int(overall_percentage)
        )

        st.write(
            f"Overall Attendance: **{overall_percentage:.2f}%**"
        )

    else:

        st.info(
            "No attendance records available yet."
        )


# ============================================================
# ADD STUDENT
# ============================================================

elif menu == "Add Student":

    st.header("➕ Add Student")

    with st.form("student_form"):

        student_id = st.text_input(
            "Student ID",
            placeholder="Example: ST001"
        )

        name = st.text_input(
            "Student Name",
            placeholder="Example: Meghana"
        )

        department = st.text_input(
            "Department",
            placeholder="Example: CSE"
        )

        year = st.selectbox(
            "Year",
            [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year"
            ]
        )

        submitted = st.form_submit_button(
            "Add Student"
        )

        if submitted:

            if not student_id or not name or not department:

                st.error(
                    "Please fill all required fields."
                )

            else:

                duplicate = any(
                    student["id"] == student_id
                    for student in students
                )

                if duplicate:

                    st.error(
                        "Student ID already exists."
                    )

                else:

                    new_student = {
                        "id": student_id,
                        "name": name,
                        "department": department,
                        "year": year
                    }

                    students.append(new_student)

                    save_students(students)

                    st.success(
                        "Student added successfully!"
                    )


# ============================================================
# MARK ATTENDANCE
# ============================================================

elif menu == "Mark Attendance":

    st.header("📝 Mark Attendance")

    if not students:

        st.warning(
            "Please add students first."
        )

    else:

        student_options = {
            f"{student['id']} - {student['name']}":
            student
            for student in students
        }

        selected_student = st.selectbox(
            "Select Student",
            list(student_options.keys())
        )

        selected_date = st.date_input(
            "Attendance Date",
            value=date.today()
        )

        status = st.radio(
            "Attendance Status",
            [
                "Present",
                "Absent"
            ],
            horizontal=True
        )

        if st.button(
            "Save Attendance"
        ):

            student = student_options[selected_student]

            attendance_record = {
                "student_id": student["id"],
                "student_name": student["name"],
                "date": str(selected_date),
                "status": status
            }

            attendance.append(
                attendance_record
            )

            save_attendance(attendance)

            st.success(
                f"Attendance marked as {status}."
            )


# ============================================================
# ATTENDANCE REPORT
# ============================================================

elif menu == "Attendance Report":

    st.header("📊 Attendance Report")

    if not students:

        st.info(
            "No students available."
        )

    else:

        for student in students:

            student_records = [
                record
                for record in attendance
                if record["student_id"] == student["id"]
            ]

            total = len(student_records)

            present = sum(
                1
                for record in student_records
                if record["status"] == "Present"
            )

            absent = sum(
                1
                for record in student_records
                if record["status"] == "Absent"
            )

            if total > 0:

                percentage = (
                    present / total
                ) * 100

            else:

                percentage = 0

            st.subheader(
                f"{student['name']} ({student['id']})"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.write(
                    f"**Total Classes:** {total}"
                )

            with col2:

                st.write(
                    f"**Present:** {present}"
                )

            with col3:

                st.write(
                    f"**Absent:** {absent}"
                )

            with col4:

                st.write(
                    f"**Attendance:** {percentage:.2f}%"
                )

            st.progress(
                int(min(percentage, 100))
            )

            st.divider()


# ============================================================
# STUDENT LIST
# ============================================================

elif menu == "Student List":

    st.header("👥 Student List")

    if not students:

        st.info(
            "No students added yet."
        )

    else:

        for student in students:

            st.write(
                f"### {student['name']}"
            )

            st.write(
                f"**Student ID:** {student['id']}"
            )

            st.write(
                f"**Department:** {student['department']}"
            )

            st.write(
                f"**Year:** {student['year']}"
            )

            st.divider()