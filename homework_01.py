import sqlite3

vehicles = [
    ("Ford", "Focus", 1000),
    ("Ford", "Mustang", 10000),
    ("Ford", "Explorer", 1500),
    ("Toyota", "Camry", 2500),
    ("Toyota", "Rav4", 1000)
]

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO inventory VALUES(?,?,?)", vehicles)