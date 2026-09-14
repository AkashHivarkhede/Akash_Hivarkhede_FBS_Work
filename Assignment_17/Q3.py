# Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


class Student:

    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def Display(self):
        print("Student ID :", self.StudentId)
        print("Name       :", self.Name)
        print("Age        :", self.Age)
        print("Percentage :", self.Percentage)
        print("Rank       :", self.CalculateRank())

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"StudentId: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, Percentage: {self.Percentage}"


class MedicalStudent(Student):

    def __init__(self, StudentId, Name, Age, Percentage,
                 Specialization, MarksOfInternship):

        super().__init__(StudentId, Name, Age, Percentage)

        self.Specialization = Specialization
        self.MarksOfInternship = MarksOfInternship

    def Accept(self):
        super().Accept()

        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Marks of Internship: "))

    def Display(self):
        super().Display()

        print("Specialization    :", self.Specialization)
        print("Marks Of Internship :", self.MarksOfInternship)

    def CalculateRank(self):

        total = self.Percentage + self.MarksOfInternship

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass"
        else:
            return "Fail"


    def __str__(self):

        return (f"StudentId: {self.StudentId}, "
                f"Name: {self.Name}, "
                f"Age: {self.Age}, "
                f"Percentage: {self.Percentage}, "
                f"Specialization: {self.Specialization}, "
                f"MarksOfInternship: {self.MarksOfInternship}")


m1 = MedicalStudent(
    201,
    "Akash",
    22,
    80,
    "Cardiology",
    75
)

m1.Display()


print("\nUsing __str__ method:")
print(m1)
