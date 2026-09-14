# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


def calculate_total_cost(age , ticket_cost):

    if age < 12:
        discount = 0.3 * ticket_cost
        final_cost = ticket_cost - discount
    elif age > 59:
        discount = 0.5 * ticket_cost
        final_cost = ticket_cost - discount
    else:
        final_cost = ticket_cost
    return final_cost


def calculate_total(passengers, ticket_cost):

    total_cost = 0

    for i in range(passengers):
        age = int(input(f"Enter age of passenger {i + 1}: "))

        cost = calculate_total_cost(age, ticket_cost)

        print(f"Cost for passenger {i + 1}: {cost}")

        total_cost += cost

    return total_cost


passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))

total_amount = calculate_total(passengers, ticket_cost)

print("\n-------------------------------")
print(f"Total amount for all passengers: {total_amount}")
print("-------------------------------")