import tkinter as tk
from tkinter import messagebox
import session

# ---------------- FUNCTIONS ----------------

def start_exam():
    root.destroy()
    import exam

def view_results():
    root.destroy()
    import results

def logout():
    session.current_user = None
    root.destroy()
    import login_register

# ---------------- USER CHECK ----------------

if not session.current_user:
    messagebox.showerror(
        "Access Denied",
        "Please login first."
    )
    import login_register
    exit()

# ---------------- GUI ----------------

root = tk.Tk()

root.title("Student Dashboard")
root.geometry("700x500")
root.configure(bg="#111827")
root.resizable(False, False)

title = tk.Label(
    root,
    text="ONLINE EXAMINATION SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#111827",
    fg="white"
)

title.pack(pady=20)

welcome = tk.Label(
    root,
    text=f"Welcome, {session.current_user}",
    font=("Arial", 16),
    bg="#111827",
    fg="white"
)

welcome.pack(pady=10)

card = tk.Frame(
    root,
    bg="#1f2937",
    padx=30,
    pady=30
)

card.pack(pady=40)

tk.Button(
    card,
    text="Start Exam",
    width=25,
    height=2,
    bg="#3b82f6",
    fg="white",
    command=start_exam
).pack(pady=10)

tk.Button(
    card,
    text="View Results",
    width=25,
    height=2,
    bg="#10b981",
    fg="white",
    command=view_results
).pack(pady=10)

tk.Button(
    card,
    text="Logout",
    width=25,
    height=2,
    bg="#ef4444",
    fg="white",
    command=logout
).pack(pady=10)

footer = tk.Label(
    root,
    text="Online Examination System",
    bg="#111827",
    fg="#9ca3af"
)

footer.pack(side="bottom", pady=10)

root.mainloop()