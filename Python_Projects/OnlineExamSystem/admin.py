import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Connection
conn = sqlite3.connect("online_exam.db")
cursor = conn.cursor()

# ---------------- ADD QUESTION ----------------
def add_question():

    question = question_entry.get("1.0", tk.END).strip()

    op1 = option1_entry.get().strip()
    op2 = option2_entry.get().strip()
    op3 = option3_entry.get().strip()
    op4 = option4_entry.get().strip()

    answer = answer_entry.get().strip()

    if not all([question, op1, op2, op3, op4, answer]):
        messagebox.showerror(
            "Error",
            "Fill all fields"
        )
        return

    cursor.execute("""
    INSERT INTO questions
    (question, option1, option2, option3, option4, answer)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (question, op1, op2, op3, op4, answer))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Question Added Successfully"
    )

    clear_fields()
    view_questions()

# ---------------- VIEW QUESTIONS ----------------
def view_questions():

    listbox.delete(0, tk.END)

    cursor.execute("""
    SELECT id, question
    FROM questions
    """)

    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(
            tk.END,
            f"{row[0]} | {row[1]}"
        )

# ---------------- DELETE QUESTION ----------------
def delete_question():

    selected = listbox.curselection()

    if not selected:
        messagebox.showerror(
            "Error",
            "Select a Question"
        )
        return

    item = listbox.get(selected[0])

    qid = item.split("|")[0].strip()

    cursor.execute(
        "DELETE FROM questions WHERE id=?",
        (qid,)
    )

    conn.commit()

    messagebox.showinfo(
        "Deleted",
        "Question Deleted"
    )

    view_questions()

# ---------------- CLEAR ----------------
def clear_fields():

    question_entry.delete(
        "1.0",
        tk.END
    )

    option1_entry.delete(0, tk.END)
    option2_entry.delete(0, tk.END)
    option3_entry.delete(0, tk.END)
    option4_entry.delete(0, tk.END)

    answer_entry.delete(0, tk.END)

# ---------------- GUI ----------------
root = tk.Tk()

root.title("Admin Panel")
root.geometry("800x650")

tk.Label(
    root,
    text="ADMIN PANEL",
    font=("Arial", 18, "bold")
).pack(pady=10)

# Question
tk.Label(
    root,
    text="Question"
).pack()

question_entry = tk.Text(
    root,
    width=70,
    height=4
)
question_entry.pack()

# Options
tk.Label(root, text="Option 1").pack()
option1_entry = tk.Entry(root, width=50)
option1_entry.pack()

tk.Label(root, text="Option 2").pack()
option2_entry = tk.Entry(root, width=50)
option2_entry.pack()

tk.Label(root, text="Option 3").pack()
option3_entry = tk.Entry(root, width=50)
option3_entry.pack()

tk.Label(root, text="Option 4").pack()
option4_entry = tk.Entry(root, width=50)
option4_entry.pack()

# Answer
tk.Label(
    root,
    text="Correct Answer"
).pack()

answer_entry = tk.Entry(
    root,
    width=50
)
answer_entry.pack()

# Buttons
tk.Button(
    root,
    text="Add Question",
    width=20,
    command=add_question
).pack(pady=5)

tk.Button(
    root,
    text="Delete Question",
    width=20,
    command=delete_question
).pack(pady=5)

tk.Button(
    root,
    text="View Questions",
    width=20,
    command=view_questions
).pack(pady=5)

# Listbox
listbox = tk.Listbox(
    root,
    width=100,
    height=15
)

listbox.pack(pady=10)

view_questions()

root.mainloop()