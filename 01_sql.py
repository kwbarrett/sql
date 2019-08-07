import sqlite3

with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE population
            (cty TEXT, state TEXT, population INT)
        """
    )