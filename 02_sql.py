# INSERT command

# import sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 84000000)")
    cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 8000000)")
