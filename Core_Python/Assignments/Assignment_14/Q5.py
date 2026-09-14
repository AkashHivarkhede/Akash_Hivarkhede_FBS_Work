# Write a Python program to find the longest common prefix of all strings. Use the Python set.

strings = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(strings[0])):
    chars = set()

    for string in strings:
        if i < len(string):
            chars.add(string[i])
        else:
            break

    if len(chars) == 1:
        prefix = prefix + strings[0][i]
    else:
        break

print("The longest common prefix is:", prefix)
