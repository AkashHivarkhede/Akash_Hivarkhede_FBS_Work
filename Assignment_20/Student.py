from SY.SYMARKS import SYMARKS
from TY.TYMarks import TYMarks


class Student:

    def __init__(self, roll_no, name, symarks, tymarks):
        self.roll_no = roll_no
        self.name = name
        self.symarks = symarks
        self.tymarks = tymarks

    def calculate_total(self):
        return self.symarks.ComputerTotal + self.tymarks.Theory

    def calculate_grade(self):
        total = self.calculate_total()

        if total >= 70:
            return "A"
        elif total >= 60:
            return "B"
        elif total >= 50:
            return "C"
        elif total >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display(self):

        total = self.calculate_total()
        grade = self.calculate_grade()

        print("\n-----------------------------")
        print("       STUDENT RESULT")
        print("-----------------------------")
        print("Roll Number :", self.roll_no)
        print("Name        :", self.name)
        print("SY Computer :", self.symarks.ComputerTotal)
        print("TY Computer :", self.tymarks.Theory)
        print("Total Marks :", total)
        print("Grade       :", grade)
        print("-----------------------------")


sy = SYMARKS(35, 40, 38)


ty = TYMarks(40, 45)

s1 = Student(101, "Akash", sy, ty)

s1.display()