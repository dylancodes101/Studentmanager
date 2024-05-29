import random as rm
from tabulate import tabulate
import input as IP
from fake_data import generate_fake_students
from csv_operations import save_students_to_csv,read_students_from_csv

def generate_students_table(students, data):
  global headers
  temp = []
  headers = set()

  for student in students:
      headers.update(student.get_attributes().keys())
  headers = sorted(headers)

  for i, header in enumerate(headers):
      temp.append([i + 1, header])
  print(tabulate(temp, headers=["#", "Attribute"]))

  sel = int(input("Sort by which attribute (enter corresponding number): ")) - 1
  sort_attribute = temp[sel][1]

  sorted_data = sorted(data, key=lambda x: int(x[sort_attribute]) if x[sort_attribute].isdigit() else x[sort_attribute], reverse=True)
  print(tabulate(sorted_data, headers='keys', tablefmt='grid'))
  
def main():
  amount_of_students = IP.Input().fake_students_amount()
  students = generate_fake_students(amount_of_students)
  if students:
      save_students_to_csv(students, "students.csv")
  data = read_students_from_csv("students.csv")
  generate_students_table(students, data)
  
if __name__ == "__main__":
  main()