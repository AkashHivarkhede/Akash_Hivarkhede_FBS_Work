# Python Program to Detect if Two Strings are Anagrams

str1 = str(input('Enter first string :'))

str2 = str(input('Enter second string :'))

if len(str1) != len(str2):
    print("The strings are not Anagrams.")
else:

    is_angram = True

    for ch in str1:
        count1 = 0 
        count2 = 0 

        for c in str1:
            if c == ch:
                count1 = count1 + 1

        for c in str2:
            if c == ch:
                count2 = count2 + 1

        if count1 != count2:
            is_angram = False
            break

    if is_angram:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")