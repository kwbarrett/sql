import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO populations VALUES('New York City','NY', 84000000)")
        cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 8000000)")
    # except sqlite3.OperationalError:
    #     print("Opps! Something went wrong. Try again..")
    except Exception as e:
        print(e)