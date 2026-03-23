import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks REAL
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def add_student():
    name = name_entry.get()
    marks = marks_entry.get()

    if name == "" or marks == "":
        messagebox.showerror("Error", "All fields required")
        return

    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()

    messagebox.showinfo("Success", "Student added")
    clear_fields()
    view_students()


def view_students():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END, f"{row[0]} | {row[1]} - {row[2]}")


def search_student():
    name = name_entry.get()
    listbox.delete(0, tk.END)

    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            listbox.insert(tk.END, f"{row[0]} | {row[1]} - {row[2]}")
    else:
        messagebox.showinfo("Result", "No student found")


def delete_student():
    selected = listbox.get(tk.ACTIVE)

    if not selected:
        messagebox.showerror("Error", "Select a student")
        return

    student_id = selected.split("|")[0].strip()

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    messagebox.showinfo("Deleted", "Student removed")
    view_students()


def clear_fields():
    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x400")

# Labels
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Marks").pack()
marks_entry = tk.Entry(root)
marks_entry.pack()

# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Search Student", command=search_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Run
view_students()
root.mainloop()