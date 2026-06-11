import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
import session

# Database Connection
conn = sqlite3.connect("online_exam.db")
cursor = conn.cursor()

# ---------------- LOAD RESULTS ----------------
def load_results():

    listbox.delete(0, tk.END)

    try:
        if session.current_user:

            cursor.execute("""
            SELECT score,
                   total_questions,
                   percentage,
                   exam_date
            FROM results
            WHERE username = ?
            ORDER BY id DESC
            """, (session.current_user,))

        else:
            cursor.execute("""
            SELECT score,
                   total_questions,
                   percentage,
                   exam_date
            FROM results
            ORDER BY id DESC
            """)

        rows = cursor.fetchall()

        if not rows:
            listbox.insert(tk.END, "No Results Found")
            return

        for row in rows:

            listbox.insert(
                tk.END,
                f"Score: {row[0]}/{row[1]}"
            )

            listbox.insert(
                tk.END,
                f"Percentage: {row[2]:.2f}%"
            )

            listbox.insert(
                tk.END,
                f"Date: {row[3]}"
            )

            listbox.insert(
                tk.END,
                "-" * 60
            )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )

# ---------------- STATISTICS ----------------
def show_stats():

    try:

        if session.current_user:

            cursor.execute("""
            SELECT MAX(score),
                   AVG(percentage)
            FROM results
            WHERE username = ?
            """, (session.current_user,))

        else:

            cursor.execute("""
            SELECT MAX(score),
                   AVG(percentage)
            FROM results
            """)

        result = cursor.fetchone()

        highest = result[0] if result[0] else 0
        average = result[1] if result[1] else 0

        messagebox.showinfo(
            "Statistics",
            f"Highest Score: {highest}\n\n"
            f"Average Percentage: {average:.2f}%"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

# ---------------- GRAPH ----------------
def show_graph():

    try:

        if session.current_user:

            cursor.execute("""
            SELECT percentage
            FROM results
            WHERE username = ?
            ORDER BY id
            """, (session.current_user,))

        else:

            cursor.execute("""
            SELECT percentage
            FROM results
            ORDER BY id
            """)

        rows = cursor.fetchall()

        if not rows:
            messagebox.showerror(
                "Error",
                "No result data available"
            )
            return

        percentages = [row[0] for row in rows]

        plt.figure(figsize=(8, 5))

        plt.plot(
            range(1, len(percentages) + 1),
            percentages,
            marker="o"
        )

        plt.title("Performance History")
        plt.xlabel("Exam Attempt")
        plt.ylabel("Percentage")
        plt.grid(True)

        plt.show()

    except Exception as e:
        messagebox.showerror(
            "Graph Error",
            str(e)
        )

# ---------------- GUI ----------------
root = tk.Tk()

root.title("Results & Analytics")
root.geometry("750x550")

title = tk.Label(
    root,
    text="RESULTS & ANALYTICS",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

user_text = session.current_user if session.current_user else "All Users"

user_label = tk.Label(
    root,
    text=f"Viewing: {user_text}",
    font=("Arial", 11)
)

user_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Load Results",
    command=load_results,
    width=20
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Statistics",
    command=show_stats,
    width=20
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Performance Graph",
    command=show_graph,
    width=20
).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(
    root,
    width=100,
    height=20
)

listbox.pack(pady=15)

load_results()

root.mainloop()