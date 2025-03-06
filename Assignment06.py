# -------------------------------------------------------------------------- #
# Title: Assignment06
# Description: This assignment demonstrates a script using functions
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# Mariusz Sokol, 3.5.2025
# -------------------------------------------------------------------------- #

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

class IO:
    """Handles all input and output operations."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays an error message.

        :param message: The custom error message.
        :param error: The exception object (optional).
        """
        print(f"Error: {message}")
        if error:
            print("-- Technical Error Message --")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu():
        """
        Displays the program menu.
        """
        print(MENU)

    @staticmethod
    def input_menu_choice():
        """
        Gets the user's menu choice.

        :return: The menu choice as a string.
        """
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Displays the list of registered students and their courses.

        :param student_data: List of dictionaries containing student details.
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in '
                  f'{student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        Collects student details from the user.

        :param student_data: List to store student records.
        """
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            student = {"FirstName": first_name, "LastName": last_name,
                       "CourseName": course_name}
            student_data.append(student)

            print(f"You have registered {first_name} {last_name} for "
                  f"{course_name}.")
        except ValueError as e:
            IO.output_error_messages("Invalid input provided.", e)
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while "
                                     "entering student data.", e)

class FileProcessor:
    """Handles reading from and writing to files."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads student data from a JSON file.

        :param file_name: The file name to read from.
        :param student_data: The list to store retrieved student records.
        """
        try:
            with open(file_name, "r") as file:
                student_data.extend(json.load(file))
        except FileNotFoundError:
            IO.output_error_messages("File not found. A new file will be "
                                     "created.")
        except json.JSONDecodeError:
            IO.output_error_messages("Error decoding JSON. Ensure the file "
                                     "is properly formatted.")
        except Exception as e:
            IO.output_error_messages("An error occurred while reading "
                                     "the file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes student data to a JSON file.

        :param file_name: The file name to write to.
        :param student_data: The list of student records to save.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            print("The following data was saved to file!")
            IO.output_student_courses(student_data)
        except Exception as e:
            IO.output_error_messages("An error occurred while writing "
                                     "to the file.", e)

# Main Program Logic
students = []
FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu()
    choice = IO.input_menu_choice()

    if choice == "1":
        IO.input_student_data(students)
    elif choice == "2":
        IO.output_student_courses(students)
    elif choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif choice == "4":
        print("Program Ended")
        break
    else:
        print("Please only choose option 1, 2, 3, or 4.")