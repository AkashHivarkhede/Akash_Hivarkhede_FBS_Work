from database.db_connection import get_connection


def waste_report():
    print("\n========== WASTE REPORT ==========")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            SUM(prepared_quantity),
            SUM(sold_quantity),
            SUM(wasted_quantity)
        FROM food_records
    """

    cursor.execute(query)

    result = cursor.fetchone()

    total_prepared = result[0] or 0
    total_sold = result[1] or 0
    total_wasted = result[2] or 0

    print(f"\nTotal Food Prepared : {total_prepared}")
    print(f"Total Food Sold     : {total_sold}")
    print(f"Total Food Wasted   : {total_wasted}")

    if total_prepared > 0:
        waste_percentage = (
            total_wasted / total_prepared
        ) * 100

        print(
            f"Waste Percentage    : "
            f"{waste_percentage:.2f}%"
        )
    else:
        print("Waste Percentage    : 0%")

    cursor.close()
    connection.close()