# Python Program to Check if a Given Key Exists in a Dictionary or Not

dict = {'Name': 'Akash', 'Age': 23, 'City': 'Pune'}

key = input("Enter the key to check: ")

if key in dict:
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.")