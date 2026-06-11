import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    issued INTEGER DEFAULT 0
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def add_book():
    title = title_entry.get()

    if title == "":
        messagebox.showerror("Error", "Enter book title")
        return

    try:
        cursor.execute("INSERT INTO books (title) VALUES (?)", (title,))
        conn.commit()
        messagebox.showinfo("Success", "Book added")
        clear_fields()
        view_books()
    except:
        messagebox.showerror("Error", "Book already exists")


def view_books():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    for row in rows:
        status = "Issued" if row[2] else "Available"
        listbox.insert(tk.END, f"{row[0]} | {row[1]} - {status}")


def issue_book():
    selected = listbox.get(tk.ACTIVE)

    if not selected:
        messagebox.showerror("Error", "Select a book")
        return

    book_id = selected.split("|")[0].strip()

    cursor.execute("SELECT issued FROM books WHERE id=?", (book_id,))
    issued = cursor.fetchone()[0]

    if issued:
        messagebox.showinfo("Info", "Already issued")
    else:
        cursor.execute("UPDATE books SET issued=1 WHERE id=?", (book_id,))
        conn.commit()
        view_books()


def return_book():
    selected = listbox.get(tk.ACTIVE)

    if not selected:
        messagebox.showerror("Error", "Select a book")
        return

    book_id = selected.split("|")[0].strip()

    cursor.execute("SELECT issued FROM books WHERE id=?", (book_id,))
    issued = cursor.fetchone()[0]

    if not issued:
        messagebox.showinfo("Info", "Not issued")
    else:
        cursor.execute("UPDATE books SET issued=0 WHERE id=?", (book_id,))
        conn.commit()
        view_books()


def delete_book():
    selected = listbox.get(tk.ACTIVE)

    if not selected:
        messagebox.showerror("Error", "Select a book")
        return

    book_id = selected.split("|")[0].strip()

    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()

    messagebox.showinfo("Deleted", "Book removed")
    view_books()


def search_book():
    title = title_entry.get()
    listbox.delete(0, tk.END)

    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            status = "Issued" if row[2] else "Available"
            listbox.insert(tk.END, f"{row[0]} | {row[1]} - {status}")
    else:
        messagebox.showinfo("Result", "No book found")


def clear_fields():
    title_entry.delete(0, tk.END)


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Library Management System (SQLite)")
root.geometry("500x400")

# Labels
tk.Label(root, text="Book Title").pack()
title_entry = tk.Entry(root)
title_entry.pack()

# Buttons
tk.Button(root, text="Add Book", command=add_book).pack(pady=5)
tk.Button(root, text="View Books", command=view_books).pack(pady=5)
tk.Button(root, text="Issue Book", command=issue_book).pack(pady=5)
tk.Button(root, text="Return Book", command=return_book).pack(pady=5)
tk.Button(root, text="Search Book", command=search_book).pack(pady=5)
tk.Button(root, text="Delete Book", command=delete_book).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Run
view_books()
root.mainloop()