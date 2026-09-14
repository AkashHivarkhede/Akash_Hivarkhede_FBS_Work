# Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.


try:
    # Accept numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Accept operator
    operator = input("Enter operator (+, -, *, /): ")

    # Check operator
    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Invalid operator")

    # Perform operation
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    print("Result =", result)


except ValueError as e:
    if str(e) == "Invalid operator":
        print("Error: Invalid operator. Please use +, -, *, or /.")
    else:
        print("Error: Invalid number. Please enter a valid number.")


except ZeroDivisionError:
    print("Error: Cannot divide by zero.")