from database.db_connection import get_connection


def add_food():
    print("\n========== ADD FOOD ==========")

    food_name = input("Food name: ")
    category = input("Category: ")

    try:
        price = float(input("Price: "))

        if price <= 0:
            print("Price must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid price.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO food_items (food_name, category, price)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (food_name, category, price))

    connection.commit()

    cursor.close()
    connection.close()

    print("\nFood added successfully!")


def view_food():
    print("\n========== FOOD ITEMS ==========")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, food_name, category, price
        FROM food_items
    """)

    foods = cursor.fetchall()

    if not foods:
        print("No food items found.")
    else:
        print("-" * 60)
        print(f"{'ID':<5}{'Food':<25}{'Category':<15}{'Price':<10}")
        print("-" * 60)

        for food in foods:
            print(
                f"{food[0]:<5}"
                f"{food[1]:<25}"
                f"{food[2]:<15}"
                f"₹{food[3]:<9}"
            )

    cursor.close()
    connection.close()


def update_food():
    view_food()

    try:
        food_id = int(input("\nEnter food ID to update: "))
        price = float(input("Enter new price: "))

        if price <= 0:
            print("Price must be greater than 0.")
            return

    except ValueError:
        print("Invalid input.")
        return

    food_name = input("Enter new food name: ")
    category = input("Enter new category: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE food_items
        SET food_name = %s,
            category = %s,
            price = %s
        WHERE id = %s
    """

    cursor.execute(
        query,
        (food_name, category, price, food_id)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("\nFood updated successfully!")
    else:
        print("\nFood ID not found.")

    cursor.close()
    connection.close()


def delete_food():
    view_food()

    try:
        food_id = int(input("\nEnter food ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM food_items WHERE id = %s",
            (food_id,)
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("\nFood deleted successfully!")
        else:
            print("\nFood ID not found.")

    except Exception as e:
        connection.rollback()
        print("\nCannot delete this food.")
        print("It may already have records.")

    cursor.close()
    connection.close()