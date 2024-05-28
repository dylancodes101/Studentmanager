-- Create the database
CREATE DATABASE student_gradebook;

-- Switch to the newly created database
USE student_gradebook;

-- Create the students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create the courses table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(10) UNIQUE NOT NULL
);

-- Create the grades table
CREATE TABLE grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade CHAR(2) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Insert example data into the students table
INSERT INTO students (first_name, last_name, date_of_birth, email)
VALUES 
('John', 'Doe', '2000-05-15', 'john.doe@example.com'),
('Jane', 'Smith', '2001-07-22', 'jane.smith@example.com'),
('Alice', 'Johnson', '1999-03-10', 'alice.johnson@example.com');

-- Insert example data into the courses table
INSERT INTO courses (course_name, course_code)
VALUES 
('Mathematics', 'MATH101'),
('History', 'HIST202'),
('Computer Science', 'CS303');

-- Insert example data into the grades table
INSERT INTO grades (student_id, course_id, grade)
VALUES 
(1, 1, 'A'),
(1, 2, 'B'),
(2, 1, 'B+'),
(2, 3, 'A-'),
(3, 2, 'C'),
(3, 3, 'B');

-- Query to view the student grades
SELECT 
    students.first_name, 
    students.last_name, 
    courses.course_name, 
    grades.grade
FROM 
    grades
JOIN 
    students ON grades.student_id = students.student_id
JOIN 
    courses ON grades.course_id = courses.course_id
ORDER BY 
    students.last_name, courses.course_name;
