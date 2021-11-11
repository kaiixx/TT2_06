import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# create users table in sqlite database
query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, name text, appointment text)"
cursor.execute(query)

connection.commit()
connection.close()
