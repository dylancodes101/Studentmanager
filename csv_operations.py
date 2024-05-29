# csv_operations.py
import csv
from student import Student

def save_students_to_csv(Students, filename):
    with open(filename, 'w', newline='') as csvfile:
        first_student_attributes = Students[0].get_attributes()
        fieldnames = first_student_attributes.keys()

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for student in Students:
            writer.writerow(student.get_attributes())

def read_students_from_csv(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data
