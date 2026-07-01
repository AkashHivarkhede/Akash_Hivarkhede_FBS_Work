# Write a program to convert days into years, weeks and days.

days = int(input('Enter days:'))

years = days // 365
days = days % 365

weeks = days // 7 
days  = days % 7 

print(f'Years: {years} , Weeks: {weeks} , Days: {days}')