# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

# Input basic salary
basic = float(input("Enter Basic Salary: "))

# Calculate allowances
DA = basic * 10 / 100
TA = basic * 12 / 100
HRA = basic * 15 / 100

# Calculate total salary
total_salary = basic + DA + TA + HRA

# Display results
print("DA =", DA)
print("TA =", TA)
print("HRA =", HRA)
print("Total Salary =", total_salary)