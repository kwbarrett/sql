import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM inventory WHERE make = 'Ford'")

    rows = cursor.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])