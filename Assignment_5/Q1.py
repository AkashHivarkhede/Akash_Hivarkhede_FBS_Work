# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


def login():
    correct_userid = "admin"
    correct_password = "admin123"
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        userid = input("Enter User ID: ")
        password = input("Enter Password: ")

        if userid == correct_userid and password == correct_password:
            print("Login successful!")
            return
        else:
            attempts += 1
            print(f"Incorrect credentials. You have {max_attempts - attempts} attempts left.")

    print("Maximum login attempts exceeded. Program terminated.")


# login()


def login1():
    userId = 'admin'
    password = 'admin123'
    for i in range(5):
        userIdInput = input("Enter User ID: ")
        passwordInput = input("Enter Password: ")

        if userIdInput == userId and passwordInput == password:
            print("Login successful!")
            return
        else:
            print(f"Incorrect credentials. You have {4 - i} attempts left.")

login1()