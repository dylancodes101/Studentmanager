import hashlib
import time
import csv
import random as rm
from tabulate import tabulate
import names as nm
import input as IP
grades = ["A","B","C","D","F"]


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = self.generate_unique_id()

    def generate_unique_id(self):
        unique_str = f"{self.first_name}{self.last_name}{self.age}{time.time()}"
        #hashed_str = hashlib.sha256(unique_str.encode()).hexdigest()
        return unique_str

    def add_attribute(self, attr_name, attr_value):
        setattr(self, attr_name, attr_value)

    def get_attributes(self):
        return self.__dict__

students = [] 

def generate_fake_students(students,amount):
    for i in range(int(amount)):
        student = Student(nm.Names().generate_name_last(),nm.Names().generate_name_first(), rm.randint(6, 13))
        students.append(student)
        students[i].add_attribute('letter_grade', rm.choice(grades))

def save_students_to_csv(students, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = students[0].get_attributes().keys()  # Get field names from the first student
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            writer.writerow(student.get_attributes())

generate_fake_students(students,IP.Input().fake_students_amount())

# Save students to a CSV file
save_students_to_csv(students, 'students.csv')

# Function to dynamically generate the student table
def generate_student_table(students):
    temp = []
    headers = set()

    # Collect all available attributes from student objects
    for student in students:
        headers.update(student.get_attributes().keys())
    headers = sorted(headers)

    # Display available attributes to the user
    for i, header in enumerate(headers):
        temp.append([i + 1, header])
    print(tabulate(temp, headers=["#", "Attribute"]))

    # Allow user to select attributes
    selected_attributes = []
    #menu config
    IP.Input().menu_config(headers, selected_attributes)
    #selected_attributes = [2,4]

    # Generate updated list of selected headers
    headers_new = [headers[i] for i in selected_attributes]
    print("Selected attributes:", headers_new)

    # Generate table using selected attributes
    table = []
    pos = 0
    for student in students:
        if pos%10 == 0 and pos != 0:
            break
        row = [getattr(student, header, None) for header in headers_new]
        table.append(row)
        pos+=1

    return headers_new, table

def find_student_by_attr(students,attr, attr_val):
    matched_students = [student for student in students if (attr_val == getattr(student, attr, None))]
    if not matched_students:
        print("No student found with the given name.")
        return None
    if len(matched_students) == 1:
        return matched_students[0]
    print("Multiple students found with that name.")
    student_data = []
    for i, student in enumerate(matched_students):
        student_data.append([i + 1, student.last_name,student.first_name, student.age, student.student_id])
    print(tabulate(student_data, headers=["#", "Last_Name", "First_Name", "Age", "Student ID"]))

    index = int(input("Enter the number of the student you want to find:")) - 1
    if 0 <= index < len(matched_students):
        return matched_students[index]
    else: 
        print("Student not found or invalid input.")

# Example usage:
headers, student_table = generate_student_table(students)
print(tabulate(student_table, headers=headers))
#add the ability to search for a student by any value
#sort ability as well
#find_student_by_attr(students, "last_name", None)
