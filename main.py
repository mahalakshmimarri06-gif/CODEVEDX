
"""
Project: Student Management System
Description: A console-based app to manage student records using JSON storage.
Author: [Your Name]
Features: Add, View, Update, Delete, JSON Persistence.
"""
import json
import os

# File name for storage
FILE_NAME = "students.json"

# Load students from file at start
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
else:
    students = {}

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")
    students[sid] = {"name": name, "grade": grade}
    save_data() # Save after change
    print(f"Student {name} added successfully!")

def view_students():
    print(f"{'ID':<15} | {'Name':<20} | {'Grade':<10}")
    print("-" * 50)
    for sid, info in students.items():
        print(f"{sid:<15} | {info['name']:<20} | {info['grade']:<10}")

def delete_student():
    sid = input("Enter the Student ID to delete: ")
    if sid in students:
        del students[sid]
        save_data() # Save after change
        print(f"Student ID {sid} has been deleted.")
    else:
        print("Error: Student ID not found.")

def update_student():
    sid = input("Enter the Student ID to update: ")
    if sid in students:
        new_name = input("Enter new name (leave blank to keep current): ")
        new_grade = input("Enter new grade (leave blank to keep current): ")
        if new_name: students[sid]['name'] = new_name
        if new_grade: students[sid]['grade'] = new_grade
        save_data() # Save after change
        print("Student details updated successfully!")
    else:
        print("Error: Student ID not found.")

# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add | 2. View | 3. Delete | 4. Update | 5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1': add_student()
    elif choice == '2': view_students()
    elif choice == '3': delete_student()
    elif choice == '4': update_student()
    elif choice == '5': break