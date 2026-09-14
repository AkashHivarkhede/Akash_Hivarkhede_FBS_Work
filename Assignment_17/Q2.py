# Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
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

    def CalculateRank(self):
        if self.Percentage >= 90:
            return "A+"
        elif self.Percentage >= 80:
            return "A"
        elif self.Percentage >= 70:
            return "B"
        elif self.Percentage >= 60:
            return "C"
        else:
            return "D"

    def __str__(self):
        return f"Student ID: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, Percentage: {self.Percentage}"


class EnggStudent(Student):

    def __init__(self, StudentId, Name, Age, Percentage, Branch, InternalMarks):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def Display(self):
        super().Display()
        print("Branch: ", self.Branch)
        print("Internal Marks: ", self.InternalMarks)

    def CalculateRank(self):
        total_marks = self.Percentage + self.InternalMarks
        if total_marks >= 180:
            return "A+"
        elif total_marks >= 160:
            return "A"
        elif total_marks >= 140:
            return "B"
        elif total_marks >= 120:
            return "C"
        else:
            return "D"

    def __str__(self):
        return f"{super().__str__()}, Branch: {self.Branch}, Internal Marks: {self.InternalMarks}"



e1 = EnggStudent(2, "Rohit", 21, 88.0, "Computer Science", 85.0)

e1.Display()

print("-----------------------")
print("Using __str__ method:")
print(e1)

