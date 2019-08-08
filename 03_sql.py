import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    cities = [
        ('Boston', 'MA', 6000000),
        ('Chicago', 'IL', 27000000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 1500000)
    ]

    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

