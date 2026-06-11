import sqlite3

conn = sqlite3.connect("online_exam.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM questions")

for row in cursor.fetchall():
    print(row)

conn.close()