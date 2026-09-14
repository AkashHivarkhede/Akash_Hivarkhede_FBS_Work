# Remove all of the vowels in a string (take input from user)


string = input("Enter a string: ")

result = [i for i in string if i.lower() not in "aeiou"]

print("String after removing vowels:", "".join(result))