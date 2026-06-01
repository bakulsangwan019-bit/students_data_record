# ============================================
#   Student Records Management System
#   MSME Technology Centre Rohtak
#   Course: Jr. Web Designer, NSQF Level-4.0
# ============================================

# List to store all student records
students = []

# -----------------------------------------------
# FUNCTION 1: Calculate Grade based on marks
# -----------------------------------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# -----------------------------------------------
# FUNCTION 2: Calculate Percentage
# -----------------------------------------------
def calculate_percentage(marks):
    # Marks are out of 100
    percentage = (marks / 100) * 100
    return round(percentage, 2)

# -----------------------------------------------
# FUNCTION 3: Add a Student Record
# -----------------------------------------------
def add_student():
    print("\n--- Add Student Record ---")

    name = input("Enter Student Name: ").strip()
    if name == "":
        print("Error: Name cannot be empty!")
        return

    roll_number = input("Enter Roll Number: ").strip()
    if roll_number == "":
        print("Error: Roll Number cannot be empty!")
        return

    # Check if roll number already exists
    for student in students:
        if student["roll_number"].lower() == roll_number.lower():
            print(f"Error: Roll Number '{roll_number}' already exists!")
            return

    try:
        marks = float(input("Enter Marks (out of 100): "))
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100!")
            return
    except ValueError:
        print("Error: Please enter a valid number for marks!")
        return

    # Calculate percentage and grade
    percentage = calculate_percentage(marks)
    grade = calculate_grade(marks)

    # Create student dictionary
    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "percentage": percentage,
        "grade": grade
    }

    # Add to list
    students.append(student)
    print(f"\nStudent '{name}' added successfully!")
    print(f"Percentage: {percentage}%  |  Grade: {grade}")

# -----------------------------------------------
# FUNCTION 4: Display All Student Records
# -----------------------------------------------
def display_all_students():
    print("\n--- All Student Records ---")

    if len(students) == 0:
        print("No records found. Please add students first.")
        return

    # Print table header
    print("-" * 65)
    print(f"{'S.No':<6} {'Name':<20} {'Roll No':<12} {'Marks':<8} {'%':<10} {'Grade'}")
    print("-" * 65)

    # Print each student
    for index, student in enumerate(students, start=1):
        print(f"{index:<6} {student['name']:<20} {student['roll_number']:<12} "
              f"{student['marks']:<8} {student['percentage']:<10} {student['grade']}")

    print("-" * 65)
    print(f"Total Students: {len(students)}")

# -----------------------------------------------
# FUNCTION 5: Search Student by Roll Number
# -----------------------------------------------
def search_student():
    print("\n--- Search Student by Roll Number ---")

    roll_number = input("Enter Roll Number to search: ").strip()

    if roll_number == "":
        print("Error: Please enter a Roll Number!")
        return

    # Search in students list
    found = None
    for student in students:
        if student["roll_number"].lower() == roll_number.lower():
            found = student
            break

    if found:
        print("\nStudent Found!")
        print("-" * 40)
        print(f"Name        : {found['name']}")
        print(f"Roll Number : {found['roll_number']}")
        print(f"Marks       : {found['marks']} / 100")
        print(f"Percentage  : {found['percentage']}%")
        print(f"Grade       : {found['grade']}")
        print("-" * 40)
    else:
        print(f"No student found with Roll Number '{roll_number}'.")

# -----------------------------------------------
# FUNCTION 6: Display Menu
# -----------------------------------------------
def display_menu():
    print("\n========================================")
    print("    Student Records Management System   ")
    print("========================================")
    print("1. Add Student Record")
    print("2. Display All Students")
    print("3. Search Student by Roll Number")
    print("4. Exit")
    print("========================================")

# -----------------------------------------------
# MAIN PROGRAM - Entry Point
# -----------------------------------------------
def main():
    print("Welcome to Student Records Management System")

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_all_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("\nThank you! Exiting the program.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()