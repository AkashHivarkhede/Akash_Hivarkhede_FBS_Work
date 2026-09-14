# Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method


class Student:

    def __init__(self, StudentId , Name  , Age , Percentage ):
        self.StudentId = StudentId
        self.Name = Name 
        self.Age = Age 
        self.Percentage = Percentage 

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Student Name: ")
        self.Age = int(input("Enter Student Age: "))
        self.Percentage = float(input("Enter Student Percentage: "))

    def Display(self):
        print("Student ID: ", self.StudentId)
        print("Student Name: ", self.Name)
        print("Student Age: ", self.Age)
        print("Student Percentage: ", self.Percentage)

    def __str__(self):
        return f"Student ID: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, Percentage: {self.Percentage}"


student1 = Student(1, "Vikas", 20, 85.5)

student1.Display()

print("-----------------------")
print("Using __str__ method:")
print(student1)