from database.db_connection import get_connection


def login():
    print("\n========== LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT id, username, role
        FROM users
        WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:
        print("\nLogin successful!")
        print(f"Welcome, {user[1]}")

        return {
            "id": user[0],
            "username": user[1],
            "role": user[2]
        }

    print("\nInvalid username or password.")
    return None