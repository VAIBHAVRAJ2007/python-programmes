import sqlite3

# Connect Database
conn = sqlite3.connect("online_exam.db")
cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'student'
)
""")

# Questions Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    answer TEXT NOT NULL
)
""")

# Results Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS results(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    score INTEGER,
    total_questions INTEGER,
    percentage REAL,
    exam_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

print("Database created successfully!")

conn.close()