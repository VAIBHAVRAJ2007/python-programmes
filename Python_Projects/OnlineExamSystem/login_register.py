import tkinter as tk
from tkinter import messagebox
import sqlite3
import session

# Database Connection
conn = sqlite3.connect("online_exam.db")
cursor = conn.cursor()

# ---------------- REGISTER ----------------
def register():
    username = reg_username.get().strip()
    password = reg_password.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

        messagebox.showinfo(
            "Success",
            "Registration Successful"
        )

        reg_username.delete(0, tk.END)
        reg_password.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error",
            "Username already exists"
        )

# ---------------- LOGIN ----------------
def login():

    username = login_username.get().strip()
    password = login_password.get().strip()

    if username == "" or password == "":
        messagebox.showerror(
            "Error",
            "Enter username and password"
        )
        return

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    if user:

        session.current_user = username

        messagebox.showinfo(
            "Success",
            f"Welcome {username}"
        )

        root.destroy()

        import dashboard

    else:

        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Online Examination System")
root.geometry("500x500")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="ONLINE EXAMINATION SYSTEM",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)

# ---------------- LOGIN FRAME ----------------
login_frame = tk.LabelFrame(
    root,
    text="Student Login",
    padx=20,
    pady=20
)
login_frame.pack(pady=10)

tk.Label(
    login_frame,
    text="Username"
).grid(row=0, column=0, pady=5)

login_username = tk.Entry(login_frame, width=25)
login_username.grid(row=0, column=1)

tk.Label(
    login_frame,
    text="Password"
).grid(row=1, column=0, pady=5)

login_password = tk.Entry(
    login_frame,
    show="*",
    width=25
)
login_password.grid(row=1, column=1)

tk.Button(
    login_frame,
    text="Login",
    width=15,
    command=login
).grid(row=2, columnspan=2, pady=10)

# ---------------- REGISTER FRAME ----------------
register_frame = tk.LabelFrame(
    root,
    text="New Registration",
    padx=20,
    pady=20
)
register_frame.pack(pady=20)

tk.Label(
    register_frame,
    text="Username"
).grid(row=0, column=0, pady=5)

reg_username = tk.Entry(register_frame, width=25)
reg_username.grid(row=0, column=1)

tk.Label(
    register_frame,
    text="Password"
).grid(row=1, column=0, pady=5)

reg_password = tk.Entry(
    register_frame,
    show="*",
    width=25
)
reg_password.grid(row=1, column=1)

tk.Button(
    register_frame,
    text="Register",
    width=15,
    command=register
).grid(row=2, columnspan=2, pady=10)

root.mainloop()