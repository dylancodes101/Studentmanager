# fake_data.py
import names as nm
import random as rm
from datetime import datetime
from student import Student

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def generate_fake_students(amount):
    Students = []
    for _ in range(int(amount)):
        student = Student(nm.get_last_name(), nm.get_first_name())
        month = rm.randint(1, 12)
        year = rm.randint(2000, 2009)  # Initialize year before the if statement
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = rm.randint(1, 31)
        elif month == 2:
            # Check if it's a leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day = rm.randint(1, 29)  # Leap year
            else:
                day = rm.randint(1, 28)  # Non-leap year
        else:
            day = rm.randint(1, 30)
        dob = Student.DOB(month, day, year)
        dob_attributes = dob.get_attributes()
        for attr_name, attr_value in dob_attributes.items():
            student.add_attribute(attr_name, attr_value)
        Students.append(student)
        student.age = calculate_age(datetime(dob.year, dob.month, dob.day))
    return Students
