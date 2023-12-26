class Student:
    def __init__(self):             #function for taking user input.
        self.rollno = input("\nEnter Roll Number: ")
        self.name = input("Enter Name: ")
        self.student_class = input("Enter Class: ")

    def display_info(self):             #function for displaying output.
        print("\nStudent Information:")
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Class:", self.student_class, "\n")

student = Student()                 #obj creation from class
student.display_info()              #calling display member to display output.
