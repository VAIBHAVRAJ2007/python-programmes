import tkinter as tk
from tkinter import messagebox
import requests

# ---------- SETTINGS ----------
TIMER = 10
timer_id = None
current_difficulty = "easy"

# ---------- GLOBALS ----------
total_questions = 0
asked_questions = 0
correct_answers = 0
performance_history = []

# ---------- FETCH ----------
def fetch_question(difficulty):
    try:
        url = f"http://127.0.0.1:5000/question/{difficulty}"
        return requests.get(url).json()
    except:
        messagebox.showerror("Error", "Server not running!")
        return None

# ---------- RESULT ----------
def show_result():
    percentage = (correct_answers / total_questions) * 100

    messagebox.showinfo(
        "Quiz Finished 🎯",
        f"Score: {correct_answers}/{total_questions}\n"
        f"Percentage: {percentage:.2f}%"
    )

    root.destroy()

# ---------- LOGIC ----------
def load_question():
    global current_question, asked_questions, time_left, timer_id

    # Stop condition
    if asked_questions >= total_questions:
        show_result()
        return

    q = fetch_question(current_difficulty)

    if not q:
        messagebox.showerror("Error", "No question found")
        root.destroy()
        return

    current_question = q
    asked_questions += 1

    question_label.config(text=f"Q{asked_questions}: {q['question']}")

    for i, option in enumerate(q["options"]):
        buttons[i].config(text=option, bg="#3b82f6", state="normal")

    difficulty_label.config(text=f"Difficulty: {current_difficulty.upper()}")

    # Timer start
    time_left = TIMER
    if timer_id:
        root.after_cancel(timer_id)

    update_timer()

def update_timer():
    global time_left, timer_id

    timer_label.config(text=f"⏱ {time_left}s")

    if time_left > 0:
        time_left -= 1
        timer_id = root.after(1000, update_timer)
    else:
        buttons[0].config(text="⏰ Time Up!", bg="orange")
        root.after(1000, next_question)

def check_answer(selected, idx):
    global correct_answers, current_difficulty, timer_id, performance_history

    # Stop timer
    if timer_id:
        root.after_cancel(timer_id)

    correct = current_question["answer"]

    for b in buttons:
        b.config(state="disabled")

    if selected == correct:
        correct_answers += 1
        buttons[idx].config(bg="green", text=f"✔ {selected}")
        performance_history.append(1)
    else:
        buttons[idx].config(bg="red", text=f"❌ {selected}")
        performance_history.append(0)

        for i, opt in enumerate(current_question["options"]):
            if opt == correct:
                buttons[i].config(bg="green", text=f"✔ {correct}")

    # Keep last 3 answers
    if len(performance_history) > 3:
        performance_history.pop(0)

    # Adaptive logic
    avg = sum(performance_history) / len(performance_history)

    if avg < 0.4:
        current_difficulty = "easy"
    elif avg < 0.7:
        current_difficulty = "medium"
    else:
        current_difficulty = "hard"

    root.after(1200, next_question)

def next_question():
    load_question()

# ---------- START ----------
def start_quiz():
    global total_questions, asked_questions, correct_answers, current_difficulty, performance_history

    try:
        total_questions = int(entry.get())
    except:
        messagebox.showerror("Error", "Enter valid number")
        return

    asked_questions = 0
    correct_answers = 0
    current_difficulty = "easy"
    performance_history = []

    start_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)

    load_question()

# ---------- UI ----------
root = tk.Tk()
root.title("Smart Quiz App")
root.geometry("700x500")
root.configure(bg="#111827")

# -------- START SCREEN --------
start_frame = tk.Frame(root, bg="#111827")
start_frame.pack(fill="both", expand=True)

card = tk.Frame(start_frame, bg="#1f2937")
card.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(card, text="🎯 Smart Quiz",
         font=("Segoe UI", 22, "bold"),
         bg="#1f2937", fg="white").pack(pady=20)

tk.Label(card, text="Number of Questions",
         bg="#1f2937", fg="white").pack()

entry = tk.Entry(card, justify="center")
entry.pack(pady=10)

def on_hover(e): e.widget.config(bg="#2563eb")
def on_leave(e): e.widget.config(bg="#3b82f6")

start_btn = tk.Button(card, text="Start Quiz",
                      font=("Segoe UI", 12, "bold"),
                      bg="#3b82f6", fg="white",
                      padx=25, pady=10,
                      command=start_quiz)
start_btn.pack(pady=20)
start_btn.bind("<Enter>", on_hover)
start_btn.bind("<Leave>", on_leave)

# -------- QUIZ SCREEN --------
quiz_frame = tk.Frame(root, bg="#111827")

top_bar = tk.Frame(quiz_frame, bg="#1f2937")
top_bar.pack(fill="x")

timer_label = tk.Label(top_bar, text="⏱ 10s",
                       bg="#1f2937", fg="#fbbf24",
                       font=("Segoe UI", 12))
timer_label.pack(side="right", padx=10, pady=10)

question_label = tk.Label(quiz_frame,
                          text="",
                          wraplength=600,
                          font=("Segoe UI", 16, "bold"),
                          bg="#111827", fg="white")
question_label.pack(pady=20)

difficulty_label = tk.Label(quiz_frame,
                            text="",
                            fg="#9ca3af",
                            bg="#111827",
                            font=("Segoe UI", 11))
difficulty_label.pack(pady=5)

buttons = []

def create_btn(i):
    btn = tk.Button(quiz_frame,
                    text="",
                    font=("Segoe UI", 11),
                    bg="#3b82f6", fg="white",
                    width=40, height=2,
                    relief="flat",
                    command=lambda: check_answer(btn.cget("text"), i))
    btn.pack(pady=8)

    btn.bind("<Enter>", lambda e: btn.config(bg="#2563eb"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#3b82f6"))

    return btn

for i in range(4):
    buttons.append(create_btn(i))

root.mainloop()