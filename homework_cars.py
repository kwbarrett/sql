import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE inventory
            (make TEXT, model TEXT, quantity INT)
        """
    )