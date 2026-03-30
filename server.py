from flask import Flask, jsonify
import sqlite3
import random

app = Flask(__name__)

def get_db():
    return sqlite3.connect("quiz.db")

@app.route("/question/<difficulty>")
def get_question(difficulty):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions WHERE difficulty=?", (difficulty,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return jsonify({})

    row = random.choice(rows)

    return jsonify({
        "question": row[1],
        "options": [row[2], row[3], row[4], row[5]],
        "answer": row[6]
    })

if __name__ == "__main__":
    app.run(debug=True)