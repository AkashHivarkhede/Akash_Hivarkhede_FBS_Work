# Python Program to Remove the Given Key from a Dictionary

dict = { 'a': 100, 'b':200, 'c':300 , 'd':400, 'e':500}

key = input("Enter the key to remove: ")

if key in dict:
    del dict[key]
    print(f"Key '{key}' has been removed from the dictionary.")
else:
    print(f"Key '{key}' not found in the dictionary.")

print("Updated dictionary:", dict)