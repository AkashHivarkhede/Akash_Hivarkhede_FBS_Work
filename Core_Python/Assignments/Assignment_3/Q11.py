# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total_amount = 0

for i in range(1, 6):
    print(f"\nPerson {i}")
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))

    if age < 12:
        # 30% discount for children
        amount = ticket - (ticket * 0.30)
    elif age > 59:
        # 50% discount for senior citizens
        amount = ticket - (ticket * 0.50)
    else:
        # Full payment for others
        amount = ticket

    print("Amount to pay =", amount)
    total_amount += amount

print("\nTotal amount for all 5 people =", total_amount)