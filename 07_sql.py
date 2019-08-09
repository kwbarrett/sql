import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cursor.execute("UPDATE population SET population = 90000000 WHERE city = 'New York City'")

    cursor.execute("DELETE from population WHERE city = 'Boston'")

    print("\nNEW DATA:\n")

    cursor.execute("SELECT * FROM population")

    rows = cursor.fetchall()

    for r in rows:
        print(r[0], r[1], r[2])
