# Find all of the words in a string that are less than 5 letters (take
# input from user)

string = input("Enter a string: ")

words = string.split()

result = [word for word in words if len(word) < 5]

print("Words with less than 5 letters:", result)