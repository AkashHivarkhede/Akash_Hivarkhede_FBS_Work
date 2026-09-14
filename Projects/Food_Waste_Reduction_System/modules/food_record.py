from database.db_connection import get_connection
from datetime import date


def add_food_record():
    print("\n========== RECORD FOOD ==========")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, food_name
        FROM food_items
    """)

    foods = cursor.fetchall()

    if not foods:
        print("No food items available.")
        cursor.close()
        connection.close()
        return

    print("\nAvailable Food:")

    for food in foods:
        print(f"{food[0]}. {food[1]}")

    try:
        food_id = int(input("\nEnter food ID: "))
        prepared = int(input("Quantity prepared: "))
        sold = int(input("Quantity sold: "))

        if prepared <= 0 or sold < 0:
            print("Invalid quantity.")
            return

        if sold > prepared:
            print("Sold quantity cannot be greater than prepared quantity.")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    wasted = prepared - sold

    record_date = date.today()

    query = """
        INSERT INTO food_records
        (food_id, record_date, prepared_quantity,
         sold_quantity, wasted_quantity)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (food_id, record_date, prepared, sold, wasted)
    )

    connection.commit()

    print("\nFood record added successfully!")
    print(f"Prepared : {prepared}")
    print(f"Sold     : {sold}")
    print(f"Wasted   : {wasted}")

    cursor.close()
    connection.close()


def view_records():
    print("\n========== FOOD RECORDS ==========")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            fr.id,
            fi.food_name,
            fr.record_date,
            fr.prepared_quantity,
            fr.sold_quantity,
            fr.wasted_quantity
        FROM food_records fr
        JOIN food_items fi
        ON fr.food_id = fi.id
        ORDER BY fr.record_date DESC
    """

    cursor.execute(query)

    records = cursor.fetchall()

    if not records:
        print("No records found.")
    else:
        print("-" * 80)

        for record in records:
            print(
                f"ID: {record[0]} | "
                f"Food: {record[1]} | "
                f"Date: {record[2]} | "
                f"Prepared: {record[3]} | "
                f"Sold: {record[4]} | "
                f"Wasted: {record[5]}"
            )

    cursor.close()
    connection.close()