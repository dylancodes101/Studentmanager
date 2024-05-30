import input as IP
from fake_data import generate_fake_students
from csv_operations import save_students_to_csv, read_students_from_csv
import Output
import student

def main():
    amount_of_students = IP.Input().fake_students_amount()
    #amount_of_students = 10
    students = generate_fake_students(amount_of_students)
    if students:
        save_students_to_csv(students, "students.csv")
    data = read_students_from_csv("students.csv")

    for info in data:
        #print(info)
        student_temp = student.Student(info)
        #print(student_temp)
        student_temp.add_attribute("hobby", "Reading")
    save_students_to_csv(students, "students.csv")
    data = read_students_from_csv("students.csv")
    #print(data)
    #print(students)
    #generate_students_table(students, data)
    Output.generate_sel_output(students, data)


if __name__ == "__main__":
    main()
