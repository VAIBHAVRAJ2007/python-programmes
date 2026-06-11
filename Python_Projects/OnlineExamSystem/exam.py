import tkinter as tk
from tkinter import messagebox
import sqlite3
import session
import random


# Database
conn = sqlite3.connect("online_exam.db")
cursor = conn.cursor()

# Load Questions
cursor.execute("""
SELECT question,
       option1,
       option2,
       option3,
       option4,
       answer
FROM questions
""")

questions = cursor.fetchall()

questions = random.sample(
    questions,
    min(10, len(questions))
)

if len(questions) == 0:
    messagebox.showerror(
        "Error",
        "No questions found.\nAdd questions from Admin Panel."
    )
    exit()

# Globals
current_question = 0
score = 0


TIMER = 30
time_left = TIMER
timer_id = None

# ---------------- SAVE RESULT ----------------
def save_result():

    total = len(questions)
    percentage = (score / total) * 100

    cursor.execute("""
    INSERT INTO results
    (username, score, total_questions, percentage)
    VALUES (?, ?, ?, ?)
    """,
    (
        session.current_user,
        score,
        total,
        percentage
    ))

    conn.commit()

# ---------------- SHOW RESULT ----------------
def show_result():

    save_result()

    percentage = (score / len(questions)) * 100

    messagebox.showinfo(
        "Exam Finished",
        f"Score: {score}/{len(questions)}\n"
        f"Percentage: {percentage:.2f}%"
    )

    root.destroy()

# ---------------- TIMER ----------------
def update_timer():

    global time_left
    global timer_id

    timer_label.config(
        text=f"⏱ {time_left}s"
    )

    if time_left > 0:

        time_left -= 1

        timer_id = root.after(
            1000,
            update_timer
        )

    else:
        next_question()

# ---------------- LOAD QUESTION ----------------
def load_question():

    global time_left
    global timer_id

    if current_question >= len(questions):
        show_result()
        return

    q = questions[current_question]

    question_label.config(
        text=f"Q{current_question+1}. {q[0]}"
    )

    selected_option.set(None) # type: ignore

    option1.config(text=q[1], value=q[1])
    option2.config(text=q[2], value=q[2])
    option3.config(text=q[3], value=q[3])
    option4.config(text=q[4], value=q[4])

    # Reset Timer
    time_left = TIMER

    if timer_id:
        root.after_cancel(timer_id)

    update_timer()

# ---------------- NEXT QUESTION ----------------
def next_question():

    global current_question
    global score

    selected = selected_option.get()

    if current_question < len(questions):

        correct_answer = questions[current_question][5]

        if selected == correct_answer:
            score += 1

    current_question += 1

    load_question()
    

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Online Examination")
root.geometry("800x500")

# Create ONLY ONE StringVar
selected_option = tk.StringVar()
selected_option.set("")

title = tk.Label(
    root,
    text="ONLINE EXAMINATION",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

timer_label = tk.Label(
    root,
    text="⏱ 30s",
    fg="red",
    font=("Arial", 14, "bold")
)
timer_label.pack()

question_label = tk.Label(
    root,
    text="",
    wraplength=700,
    font=("Arial", 14)
)
question_label.pack(pady=20)

option1 = tk.Radiobutton(
    root,
    text="",
    variable=selected_option
)
option1.pack(anchor="w", padx=100)

option2 = tk.Radiobutton(
    root,
    text="",
    variable=selected_option
)
option2.pack(anchor="w", padx=100)

option3 = tk.Radiobutton(
    root,
    text="",
    variable=selected_option
)
option3.pack(anchor="w", padx=100)

option4 = tk.Radiobutton(
    root,
    text="",
    variable=selected_option
)
option4.pack(anchor="w", padx=100)

next_btn = tk.Button(
    root,
    text="Next Question",
    command=next_question,
    width=20
)
next_btn.pack(pady=30)

load_question()

root.mainloop()