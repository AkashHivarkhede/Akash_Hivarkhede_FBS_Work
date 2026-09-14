from modules.login import login
from modules.food import (
    add_food,
    view_food,
    update_food,
    delete_food
)
from modules.food_record import (
    add_food_record,
    view_records
)
from modules.report import waste_report


def main_menu(user):

    while True:

        print("\n")
        print("=" * 45)
        print("      FOOD WASTE REDUCTION SYSTEM")
        print("=" * 45)
        print(f"Logged in as: {user['username']}")
        print("-" * 45)

        print("1. Add Food")
        print("2. View Food")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. Record Daily Food")
        print("6. View Food Records")
        print("7. Waste Report")
        print("8. Logout")

        print("-" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_food()

        elif choice == "2":
            view_food()

        elif choice == "3":
            update_food()

        elif choice == "4":
            delete_food()

        elif choice == "5":
            add_food_record()

        elif choice == "6":
            view_records()

        elif choice == "7":
            waste_report()

        elif choice == "8":
            print("\nLogged out successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


def main():

    print("\n")
    print("=" * 45)
    print("      WELCOME TO FOOD WASTE SYSTEM")
    print("=" * 45)

    user = login()

    if user:
        main_menu(user)


if __name__ == "__main__":
    main()