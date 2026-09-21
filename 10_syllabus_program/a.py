# Write a Python program to create a table named student with id, name and spi data

import sqlite3

# Connect to database (creates the file if it doesn't exist)
connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# SQL query to create the table (written as a string, executed via Python)
create_table_query = """
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    spi REAL
)
"""

cursor.execute(create_table_query)

print("Table 'student' created successfully.")

connection.commit()
connection.close()