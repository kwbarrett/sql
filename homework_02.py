import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    cursor.execute("UPDATE inventory SET quantity = 1501 WHERE quantity = 1500")
    cursor.execute("UPDATE inventory SET quantity = 2501 WHERE quantity = 2500")

    cursor.execute("SELECT * FROM inventory")

    rows = cursor.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])
