# Display the list of students having spi greater than 8

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

print("Students with SPI greater than 8:")
cursor.execute("SELECT * FROM student WHERE spi > 8")
results = cursor.fetchall()

for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, SPI: {row[2]}")

connection.commit()
connection.close()