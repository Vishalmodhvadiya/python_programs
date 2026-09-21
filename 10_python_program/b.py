# Insert data in student table

import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# ---------- (Recreate table in case this runs standalone) ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    spi REAL
)
""")

# ---------- b) Insert data into student table ----------
students_data = [
    (1, "Alice", 9.2),
    (2, "Bob", 7.5),
    (3, "Charlie", 8.8),
    (4, "David", 6.9),
    (5, "Eva", 8.1)
]

insert_query = "INSERT INTO student (id, name, spi) VALUES (?, ?, ?)"

try:
    cursor.executemany(insert_query, students_data)
    connection.commit()
    print("Data inserted successfully.\n")
except sqlite3.IntegrityError:
    print("Data already exists (duplicate id) — skipping insert.\n")

connection.commit()
connection.close()