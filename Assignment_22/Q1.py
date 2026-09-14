# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.


import pickle

class Emp:

    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f"ID: {self.eid}, Name: {self.ename}, Basic: {self.basic}"


# Add Record
def add_record():
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp = Emp(eid, ename, basic)

    with open("employee.dat", "ab") as file:
        pickle.dump(emp, file)

    print("Record added successfully.")


def read_records():
    employees = []

    try:
        with open("employee.dat", "rb") as file:
            while True:
                try:
                    emp = pickle.load(file)
                    employees.append(emp)
                except EOFError:
                    break

    except FileNotFoundError:
        pass

    return employees


def search_record():
    eid = int(input("Enter Employee ID to search: "))

    employees = read_records()

    for emp in employees:
        if emp.eid == eid:
            print("Record Found:")
            print(emp)
            return

    print("Record not found.")


def delete_record():
    eid = int(input("Enter Employee ID to delete: "))

    employees = read_records()

    found = False

    for emp in employees:
        if emp.eid == eid:
            employees.remove(emp)
            found = True
            break

    if found:
        with open("employee.dat", "wb") as file:
            for emp in employees:
                pickle.dump(emp, file)

        print("Record deleted successfully.")
    else:
        print("Record not found.")


# Edit Record
def edit_record():
    eid = int(input("Enter Employee ID to edit: "))

    employees = read_records()

    found = False

    for emp in employees:
        if emp.eid == eid:

            emp.ename = input("Enter New Employee Name: ")
            emp.basic = float(input("Enter New Basic Salary: "))

            found = True
            break

    if found:
        with open("employee.dat", "wb") as file:
            for emp in employees:
                pickle.dump(emp, file)

        print("Record updated successfully.")
    else:
        print("Record not found.")


def display_records():

    employees = read_records()

    if len(employees) == 0:
        print("No records found.")
    else:
        print("\nEmployee Records")
        print("-----------------------------")

        for emp in employees:
            print(emp)

while True:

    print("\n========== MENU ==========")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_record()

    elif choice == 2:
        search_record()

    elif choice == 3:
        delete_record()

    elif choice == 4:
        edit_record()

    elif choice == 5:
        display_records()

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")