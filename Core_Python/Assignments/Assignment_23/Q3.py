# Design a basic calculator to perform +,-,/,*


import tkinter as tk
from tkinter import messagebox


# Calculator function
def calculate():

    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        operator = operator_entry.get()

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return

            result = num1 / num2

        else:
            messagebox.showerror(
                "Error",
                "Invalid operator. Use +, -, * or /"
            )
            return

        result_label.config(text="Result = " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# Create window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x350")


# Title
title_label = tk.Label(
    root,
    text="Basic Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)


# First number
tk.Label(root, text="Enter First Number:").pack()

first_entry = tk.Entry(root)
first_entry.pack(pady=5)


# Second number
tk.Label(root, text="Enter Second Number:").pack()

second_entry = tk.Entry(root)
second_entry.pack(pady=5)


# Operator
tk.Label(root, text="Enter Operator (+, -, *, /):").pack(pady=5)

operator_entry = tk.Entry(root)
operator_entry.pack(pady=5)


# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate",
    command=calculate
)
calculate_button.pack(pady=20)


result_label = tk.Label(
    root,
    text="Result = ",
    font=("Arial", 14, "bold")
)
result_label.pack()


root.mainloop()