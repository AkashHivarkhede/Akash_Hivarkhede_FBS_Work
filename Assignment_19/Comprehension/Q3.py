# Count the number of spaces in a string (take input from user)

string = input("Enter a string: ")

spaces = [i for i in string if i == " "]

print("Number of spaces:", len(spaces))