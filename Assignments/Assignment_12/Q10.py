# Python Program to Take in Two Strings and Display the Larger String 
# without Using Built-in Functions

str1 = str(input('Enter a String1 :'))

str2 = str(input('Enter a String2 :'))


count1 = 0
count2 = 0

for ch in str1:
    count1 += 1 

for ch in str2:
    count2 += 1 

if count1 > count2:
    print('Larger string =' , str1)
elif count2 > count1:
    print('Larger string =' , str2)
else:
    print('Both string are of equal length.')