import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="food_waste_db"
    )

    return connection