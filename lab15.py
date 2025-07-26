# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 18:14:11 2025

@author: LENOVO
"""

import sqlite3

def create_connection():
    return sqlite3.connect('student_record.db')

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_record (
            Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            Subject TEXT NOT NULL,
            Mark INTEGER NOT NULL
        )
    ''')
    conn.commit()

def insert_students(conn, student_records):
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO student_record (Enrollment, name, Subject, Mark)
        VALUES (?, ?, ?, ?)
    ''', student_records)
    conn.commit()

def fetch_all_students(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_record')
    return cursor.fetchall()

def fetch_students_high_marks(conn, threshold=90):
    cursor = conn.cursor()
    cursor.execute('SELECT name, Subject, Mark FROM student_record WHERE Mark > ?', (threshold,))
    return cursor.fetchall()

def update_mark(conn, name, subject, new_mark):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE student_record SET Mark = ?
        WHERE name = ? AND Subject = ?
    ''', (new_mark, name, subject))
    conn.commit()

def delete_student(conn, name):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM student_record WHERE name = ?', (name,))
    conn.commit()

def calculate_average_mark(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(Mark) FROM student_record')
    return cursor.fetchone()[0]

def close_connection(conn):
    conn.close()

# Post Lab: Enroll a student in multiple subjects
def enroll_multiple_subjects(conn, name, subjects_marks):
    """
    subjects_marks is a list of tuples: [(subject1, mark1), (subject2, mark2), ...]
    Enrollment will be auto-incremented, so pass None as Enrollment.
    """
    cursor = conn.cursor()
    for subject, mark in subjects_marks:
        cursor.execute('''
            INSERT INTO student_record (Enrollment, name, Subject, Mark)
            VALUES (NULL, ?, ?, ?)
        ''', (name, subject, mark))
    conn.commit()

# Main program demonstrating all operations:
def main():
    conn = create_connection()
    create_table(conn)

    # Insert initial student records
    students = [
        (92301733016,'ASHUTOSH KUMAR SINGH','PWP',95),
        (92301733017,'HARSH VISHALBHAI TRIVEDI','PWP',85),
        (92301733027,'VIRAJ PRAKASHBHAI VAGHASIYA','PWP',90),
        (92301733046,'SHIVAM ATULKUMAR BHATT', 'PWP',93),
        (92301733058,'DEVENDRASINH DOLATSINH JADEJA','PWP',75)
    ]

    # Before inserting, let's check if database already has records to avoid duplicates
    existing_students = fetch_all_students(conn)
    if not existing_students:
        insert_students(conn, students)
        print("Inserted initial student records.\n")

    # Fetch and display all students
    print("All Student Records:")
    for row in fetch_all_students(conn):
        print(row)

    # Fetch students with marks > 90
    print("\nStudents with Marks greater than 90:")
    for student in fetch_students_high_marks(conn):
        print(student)

    # Update mark
    update_mark(conn, 'ASHUTOSH KUMAR SINGH', 'PWP', 98)
    cursor = conn.cursor()
    cursor.execute('SELECT name, Mark FROM student_record WHERE name = ?', ('ASHUTOSH KUMAR SINGH',))
    updated = cursor.fetchone()
    print(f"\nUpdated Mark for {updated[0]}: {updated[1]}")

    # Delete a student
    delete_student(conn, 'DEVENDRASINH DOLATSINH JADEJA')
    cursor.execute('SELECT * FROM student_record WHERE name = ?', ('DEVENDRASINH DOLATSINH JADEJA',))
    deleted = cursor.fetchone()
    if deleted is None:
        print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")

    # Calculate average mark
    avg_mark = calculate_average_mark(conn)
    print(f"\nThe average mark of students is: {avg_mark:.2f}")

    # Post Lab: Enroll a student in multiple subjects
    print("\nEnrolling new student in multiple subjects:")
    enroll_multiple_subjects(conn, 'NEW STUDENT', [('Math', 88), ('Physics', 92), ('Chemistry', 85)])
    cursor.execute('SELECT * FROM student_record WHERE name = ?', ('NEW STUDENT',))
    for record in cursor.fetchall():
        print(record)

    # Close DB connection
    close_connection(conn)

if __name__ == '__main__':
    main()
