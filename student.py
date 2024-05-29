#student.py
import time
import hashlib

class Student:
    def __init__(self, last_name, first_name, age=None):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.student_id = self.generate_unique_id()

    def add_attribute(self, attr_name, attr_value):
        setattr(self, attr_name, attr_value)

    def generate_unique_id(self):
        unique_str = f"{self.first_name}{self.last_name}{time.time()}"
        #hashed_str = hashlib.sha256(unique_str.encode()).hexdigest()
        return unique_str

    def get_attributes(self):
        return self.__dict__

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
