# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = float(input('Enter marks of subject 1: '))
m2 = float(input('Enter marks of subject 2: '))
m3 = float(input('Enter marks of subject 3: '))
m4 = float(input('Enter marks of subject 4: '))
m5 = float(input('Enter marks of subject 5: '))

# calculate total percentage 

total = m1 + m2 + m3 + m4 + m5

percentage = total / 5

print(f'Total Marks: {total}')
print(f'Percentage: {percentage}')

# Display grade 

if(percentage >= 75):
    print("Distinction")
elif(percentage >= 60):
    print('First Class')
elif(percentage >= 50):
    print('Second Class')
elif(percentage >= 35):
    print('Pass Class')
else:
    print('Fail')
