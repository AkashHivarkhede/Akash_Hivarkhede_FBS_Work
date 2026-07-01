# WAP to calculate selling price of book based on cost price and discount.

# Input cost price and discount percentage
CP = float(input("Enter Cost Price of the book: "))
D = float(input("Enter Discount Percentage: "))

# Calculate discount amount
discount = (CP * D) / 100

# Calculate selling price
SP = CP - discount

# Display result
print("Selling Price of the book =", SP)