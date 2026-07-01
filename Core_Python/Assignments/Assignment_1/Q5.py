# Write a program to enter P, T, R and calculate simple Interest.
P = float(input('Enter Principle Amount '))
R = float(input('Enter Rate of Interest '))
T = float(input('Enter Time '))

SI = (P * R * T) / 100 

print(f'Simple Interest Is {SI}')