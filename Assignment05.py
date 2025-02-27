# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Mariusz Sokol,2/25/2025, Added error handling
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
json_data: str = ''
file: None = None
menu_choice: str = ''
student_data: dict = {}
students: list = []

# Attempt to read file data
try:
    file = open(FILE_NAME, "r", encoding="utf-8")
    students = json.load(file)  # Expecting JSON format
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    students = []
except json.JSONDecodeError as e:
    print("Error: The file is not in a valid JSON format.\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    students = []
except PermissionError as e:
    print("Error: Permission denied when accessing the file.\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    students = []
except UnicodeDecodeError as e:
    print("Error: The file contains invalid encoding. Ensure it is UTF-8 "
          "encoded.\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    students = []
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    students = []
finally:
    if 'file' in locals() and not file.closed:
        file.close()

# Present and Process the data
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":  # Register a student
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ").strip()
            if not student_first_name or not student_last_name or not course_name:
                raise ValueError("All fields must be filled!")
            student_data = {"FirstName": student_first_name, "LastName":
                student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name}"
                  f"for {course_name}.")
        except ValueError as ve:
            print(ve)
            print("-- Technical Error Message -- ")
            print(ve.__doc__)
            print(ve.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    elif menu_choice == "2":  # Show data
        print("-" * 50)
        if students:
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']}"
                      f"is enrolled in {student['CourseName']}")
        else:
            print("No students registered yet.")
        print("-" * 50)
        continue

    elif menu_choice == "3":  # Save data
        try:
            file = open(FILE_NAME, "w", encoding="utf-8")
            json.dump(students, file, indent=4)
            file.close()
            print("Data successfully saved! Here is what was stored:")
            for index, student in enumerate(students, start=1):
                print(
                    f"{index}. First Name: {student.get('FirstName', 'N/A')},"
                    f"Last Name: {student.get('LastName', 'N/A')}, Course: "
                    f"{student.get('CourseName', 'N/A')}")
                json.dump(students, file, indent=4)
            print("Data successfully saved!")
        except FileNotFoundError:
            print(f"Error: The file '{FILE_NAME}' could not be found.")
        except IOError:
            print(f"Error: Unable to write to file '{FILE_NAME}'."
                  f"Please check file permissions.")
        except Exception as e:
            print(f"Error saving data: {e}")
        continue

    elif menu_choice == "4":  # Exit program
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")

print("Program Ended")
