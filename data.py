import json
import os


DATA_FOLDER = "data"

STUDENTS_FILE = os.path.join(DATA_FOLDER, "students.json")
ATTENDANCE_FILE = os.path.join(DATA_FOLDER, "attendance.json")


def create_data_files():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    if not os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "w") as file:
            json.dump([], file, indent=4)

    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w") as file:
            json.dump([], file, indent=4)


def load_students():
    create_data_files()

    with open(STUDENTS_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    create_data_files()

    with open(STUDENTS_FILE, "w") as file:
        json.dump(students, file, indent=4)


def load_attendance():
    create_data_files()

    with open(ATTENDANCE_FILE, "r") as file:
        return json.load(file)


def save_attendance(attendance):
    create_data_files()

    with open(ATTENDANCE_FILE, "w") as file:
        json.dump(attendance, file, indent=4)