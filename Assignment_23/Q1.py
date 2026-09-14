# Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.


import tkinter as tk
from tkinter import messagebox


# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check username and password
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")


# Create window
root = tk.Tk()
root.title("Login System")
root.geometry("350x250")


# Username
username_label = tk.Label(root, text="Username")
username_label.pack(pady=10)

username_entry = tk.Entry(root)
username_entry.pack()


# Password
password_label = tk.Label(root, text="Password")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack()


# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)


# Run application
root.mainloop()