# Write a program to calculate the percentage of student based on marks of any 5
# subjects.

sub1 = float(input('Enter marks of subject 1:'))
sub2 = float(input('Enter marks of subject 2:'))
sub3 = float(input('Enter marks of subject 3:'))
sub4 = float(input('Enter marks of subject 4:'))
sub5 = float(input('Enter marks of subject 5:'))

total = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total / 500) * 100

print(f'Total Marks : {total}')
print(f'Percentage : {percentage}')