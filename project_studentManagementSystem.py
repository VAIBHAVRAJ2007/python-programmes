import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks REAL
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def add_student():
    student_id = id_entry.get().strip()
    name = name_entry.get().strip()
    marks = marks_entry.get().strip()

    if student_id == "" or name == "" or marks == "":
        messagebox.showerror("Error", "All fields required")
        return

    try:
        student_id = int(student_id)
        marks = float(marks)
    except:
        messagebox.showerror("Error", "Invalid ID or Marks")
        return

    # Check if ID already exists
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    if cursor.fetchone():
        messagebox.showerror("Error", "ID already exists")
        return

    cursor.execute(
        "INSERT INTO students (id, name, marks) VALUES (?, ?, ?)",
        (student_id, name, marks)
    )
    conn.commit()

    messagebox.showinfo("Success", "Student added with ID")
    clear_fields()
    view_students()

def view_students():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END, f"ID:{row[0]} | {row[1]} → {row[2]}")


def search_student():
    name = name_entry.get()
    listbox.delete(0, tk.END)

    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            listbox.insert(tk.END, f"ID:{row[0]} | {row[1]} → {row[2]}")
    else:
        messagebox.showinfo("Result", "No student found")


def delete_student():
    student_id = id_entry.get().strip()

    if student_id == "":
        messagebox.showerror("Error", "Enter ID to delete")
        return

    try:
        student_id = int(student_id)   # 🔥 FIX
    except:
        messagebox.showerror("Error", "Invalid ID")
        return

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    if not cursor.fetchone():
        messagebox.showerror("Error", "ID not found")
        return

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    messagebox.showinfo("Deleted", "Student removed")
    clear_fields()
    view_students()


def update_student():
    student_id = id_entry.get().strip()
    name = name_entry.get().strip()
    marks = marks_entry.get().strip()

    if student_id == "" or name == "" or marks == "":
        messagebox.showerror("Error", "All fields required")
        return

    try:
        student_id = int(student_id)   # 🔥 FIX
        marks = float(marks)
    except:
        messagebox.showerror("Error", "Invalid ID or Marks")
        return

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    if not cursor.fetchone():
        messagebox.showerror("Error", "ID not found")
        return

    cursor.execute(
        "UPDATE students SET name=?, marks=? WHERE id=?",
        (name, marks, student_id)
    )
    conn.commit()

    messagebox.showinfo("Updated", "Student updated")
    clear_fields()
    view_students()


def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


# -------- AUTO-FILL FROM LIST --------
def fill_fields(event):
    selected = listbox.get(tk.ACTIVE)

    if selected:
        parts = selected.split("|")
        student_id = parts[0].replace("ID:", "").strip()
        name = parts[1].split("→")[0].strip()
        marks = parts[1].split("→")[1].strip()

        id_entry.delete(0, tk.END)
        id_entry.insert(0,student_id)
        
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)

        marks_entry.delete(0, tk.END)
        marks_entry.insert(0, marks)


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")
root.config(bg="#1e293b")

# -------- CARD --------
frame = tk.Frame(root, bg="#334155", padx=20, pady=20)
frame.pack(pady=20)

tk.Label(frame, text="🎓 Student Manager",
         font=("Segoe UI", 18, "bold"),
         bg="#334155", fg="white").grid(row=0, columnspan=2, pady=10)

# ID
tk.Label(frame, text="ID", bg="#334155", fg="white").grid(row=1, column=0)
id_entry = tk.Entry(frame)
id_entry.grid(row=1, column=1, pady=5)
def validate_id(P):
            return P.isdigit() or P == ""

vcmd = (root.register(validate_id), '%P')
id_entry.config(validate="key", validatecommand=vcmd)

# Name
tk.Label(frame, text="Name", bg="#334155", fg="white").grid(row=2, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=2, column=1, pady=5)

# Marks
tk.Label(frame, text="Marks", bg="#334155", fg="white").grid(row=3, column=0)
marks_entry = tk.Entry(frame)
marks_entry.grid(row=3, column=1, pady=5)

# -------- BUTTONS --------
btn_frame = tk.Frame(root, bg="#1e293b")
btn_frame.pack()

def style(btn):
    btn.config(bg="#3b82f6", fg="white", width=15, relief="flat")

buttons = [
    ("Add", add_student),
    ("View", view_students),
    ("Search", search_student),
    ("Update", update_student),
    ("Delete", delete_student),
    ("Clear", clear_fields)
]

for i, (text, cmd) in enumerate(buttons):
    b = tk.Button(btn_frame, text=text, command=cmd)
    style(b)
    b.grid(row=i//3, column=i%3, padx=5, pady=5)

# -------- LISTBOX + SCROLL --------
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=60, height=10, yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

listbox.bind("<<ListboxSelect>>", fill_fields)

# -------- RUN --------
view_students()
root.mainloop()