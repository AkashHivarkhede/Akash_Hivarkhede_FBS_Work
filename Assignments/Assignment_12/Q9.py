# Python Program to Calculate the Number of Words and the Number of Characters Present in a String

string = str(input('Enter a String :'))

wordCount = 0 
charCount = 0

for i in string:
    charCount = charCount + 1
    if i == ' ':
        wordCount = wordCount + 1 

print('Characters Present in a String is ', charCount)
print('Number of Words Presnet in a String is ', wordCount)


