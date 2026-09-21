# Create a table Course with id, name and student id.

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

cursor.execute("""
CREATE TABLE IF NOT EXISTS course (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES student(id)
)
""")
print("\nTable 'course' created successfully.")

connection.commit()
connection.close()