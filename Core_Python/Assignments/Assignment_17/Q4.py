# Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method


class Student:

    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def __str__(self):
        return (f"StudentId: {self.StudentId}, "
                f"Name: {self.Name}, "
                f"Age: {self.Age}, "
                f"Percentage: {self.Percentage}")


class College:


    def __init__(self, number):
        self.students = []
        self.number = number


    def AddStudent(self, student):
        if len(self.students) < self.number:
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("College is full.")


    def GetStudent(self, StudentId):
        for student in self.students:
            if student.StudentId == StudentId:
                return student

        return None

   
    def RemoveStudent(self, StudentId):
        student = self.GetStudent(StudentId)

        if student is not None:
            self.students.remove(student)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    def __str__(self):
        result = "College Students:\n"

        for student in self.students:
            result = result + str(student) + "\n"

        return result



s1 = Student(101, "Akash", 22, 80.5)
s2 = Student(102, "Rahul", 21, 75.5)
s3 = Student(103, "Priya", 22, 88.5)

c1 = College(3)


c1.AddStudent(s1)
c1.AddStudent(s2)
c1.AddStudent(s3)


print("\nGet Student:")
student = c1.GetStudent(102)

if student is not None:
    print(student)
else:
    print("Student not found.")

print("\nAll Students:")
print(c1)


c1.RemoveStudent(102)

print("\nAfter Removing Student:")
print(c1)