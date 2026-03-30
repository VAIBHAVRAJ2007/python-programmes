import tkinter as tk
from tkinter import messagebox
import random
import string

# -------- Password Generator --------
def generate_password():
    try:
        length = int(length_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid number")
        return

    characters = ""

    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one option")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# -------- Copy Function --------
def copy_password():
    password = result_entry.get()
    if password == "":
        messagebox.showerror("Error", "No password to copy")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard")

# -------- GUI --------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

# Length
tk.Label(root, text="Password Length").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# Options
var_upper = tk.IntVar()
var_lower = tk.IntVar()
var_digits = tk.IntVar()
var_symbols = tk.IntVar()

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=var_upper).pack()
tk.Checkbutton(root, text="Lowercase (a-z)", variable=var_lower).pack()
tk.Checkbutton(root, text="Numbers (0-9)", variable=var_digits).pack()
tk.Checkbutton(root, text="Symbols (!@#)", variable=var_symbols).pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result
result_entry = tk.Entry(root, width=30)
result_entry.pack(pady=5)

tk.Button(root, text="Copy", command=copy_password).pack(pady=5)

root.mainloop()