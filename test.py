import csv
import time

class Student:
    def __init__(self, last_name, first_name=None, age=None, student_id=None, month=None, day=None, year=None, **kwargs):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.student_id = student_id if student_id else self.generate_unique_id()
        self.dob = self.DOB(month, day, year) if month and day and year else None

        # Store any additional attributes in a dictionary
        self.additional_attributes = kwargs

    def add_attribute(self, attr_name, attr_value):
        self.additional_attributes[attr_name] = attr_value

    def generate_unique_id(self):
        unique_str = f"{self.first_name}{self.last_name}{time.time()}"
        return unique_str

    def get_attributes(self):
        attributes = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "age": self.age,
            "student_id": self.student_id
        }
        if self.dob:
            dob_attributes = self.dob.get_attributes()
            attributes.update(dob_attributes)

        # Include additional attributes in the output
        attributes.update(self.additional_attributes)

        return attributes

    class DOB:
        def __init__(self, month, day, year, format=None):
            self.month = month
            self.day = day
            self.year = year
            self.format = format

        def __str__(self):
            return f"{self.month:02d}/{self.day:02d}/{self.year}"

        def get_attributes(self):
            return {'month': self.month,
                    'day': self.day,
                    'year': self.year}

# Function to write students to a CSV file
def write_students_to_csv(students, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = set()
        for student in students:
            fieldnames.update(student.get_attributes().keys())
        fieldnames = sorted(fieldnames)

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student.get_attributes())

# Function to read students from a CSV file
def read_students_from_csv(filename):
    students = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_kwargs = {key: value for key, value in row.items() if key not in ['month', 'day', 'year']}
            if 'month' in row and 'day' in row and 'year' in row:
                student_kwargs['month'] = row['month']
                student_kwargs['day'] = row['day']
                student_kwargs['year'] = row['year']
            students.append(Student(**student_kwargs))
    return students

# Example usage
def main():
    # Create a list of student instances
    students = [
        Student("Doe", "John", 20, month=5, day=29, year=2000, major="Computer Science"),
        Student("Smith", "Jane", 22, month=6, day=15, year=1998, major="Mathematics")
    ]

    # Write students to CSV
    write_students_to_csv(students, 'students.csv')

    # Read students from CSV
    students_from_csv = read_students_from_csv('students.csv')

    # Add a new attribute to the first student
    if students_from_csv:
        students_from_csv[0].add_attribute('GPA', '3.8')

    # Write updated students back to CSV
    write_students_to_csv(students_from_csv, 'students_updated.csv')

    # Print updated student attributes
    for student in students_from_csv:
        print("Updated Student attributes:", student.get_attributes())

if __name__ == "__main__":
    main()
