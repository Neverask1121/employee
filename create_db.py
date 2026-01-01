import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dob TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conn.commit()
conn.close()