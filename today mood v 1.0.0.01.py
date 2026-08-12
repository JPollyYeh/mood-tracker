import tkinter as tk
from tkinter import ttk
from datetime import date
import csv


# -----------------------
# SAVE MOOD
# -----------------------

def record_mood(mood):
    today = date.today()

    with open("moods.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, mood])

    message_label.config(
        text=f"Your mood for {today} has been recorded!\nTry another tab!"
    )


# -----------------------
# SAVE PERSONALITY
# -----------------------

def record_personality(personality):
    today = date.today()

    with open("personality.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, personality])

    quiz_message_label.config(
        text="Your personality has been recorded.\nThank you for visiting."
    )


# -----------------------
# MAKE WINDOW
# -----------------------

window = tk.Tk()
window.title("My Little Daily App")
window.geometry("500x400")


# -----------------------
# MAKE TABS
# -----------------------

tabs = ttk.Notebook(window)

mood_tab = ttk.Frame(tabs)
fun_tab = ttk.Frame(tabs)
quiz_tab = ttk.Frame(tabs)

tabs.add(mood_tab, text="Mood")
tabs.add(fun_tab, text="Fun")
tabs.add(quiz_tab, text="Personality Quiz")

tabs.pack(expand=True, fill="both")


# -----------------------
# MOOD TAB
# -----------------------

title = tk.Label(
    mood_tab,
    text="How are you feeling today?",
    font=("Arial", 18),
    foreground="gray2",
    background="pink"
)

title.pack(pady=20)


happy_button = tk.Button(
    mood_tab,
    text="Happy 😊",
    font=("Arial", 18),
    command=lambda: record_mood("happy")
)
happy_button.pack(pady=5)


sad_button = tk.Button(
    mood_tab,
    text="Sad",
    font=("Arial", 18),
    command=lambda: record_mood("sad")
)
sad_button.pack(pady=5)


angry_button = tk.Button(
    mood_tab,
    text="Angry",
    font=("Arial", 18),
    command=lambda: record_mood("angry")
)
angry_button.pack(pady=5)


hurt_button = tk.Button(
    mood_tab,
    text="Hurt",
    font=("Arial", 18),
    command=lambda: record_mood("hurt")
)
hurt_button.pack(pady=5)


message_label = tk.Label(
    mood_tab,
    text=""
)

message_label.pack(pady=20)


# -----------------------
# FUN TAB
# -----------------------

fun_label = tk.Label(
    fun_tab,
    text=(
        "I want to build a choose your own adventure,\n"
        "but I'm not good enough...\n"
        "When I become good enough, I'll post it,\n"
        "and we can all play together."
    ),
    font=("Arial", 18),
    background="pink"
)

fun_label.pack(pady=50)


# -----------------------
# PERSONALITY QUIZ TAB
# -----------------------

quiz_label = tk.Label(
    quiz_tab,
    text=(
        "Personality quizzes are easier to make,\n"
        "but I have a lot to learn before I can make one."
    ),
    font=("Arial", 18),
    background="pink"
)

quiz_label.pack(pady=30)


extrovert_button = tk.Button(
    quiz_tab,
    text="Extrovert",
    font=("Arial", 18),
    command=lambda: record_personality("extrovert")
)

extrovert_button.pack(pady=5)


introvert_button = tk.Button(
    quiz_tab,
    text="Introvert",
    font=("Arial", 18),
    command=lambda: record_personality("introvert")
)

introvert_button.pack(pady=5)


quiz_message_label = tk.Label(
    quiz_tab,
    text=""
)

quiz_message_label.pack(pady=20)


# -----------------------
# START PROGRAM
# -----------------------

window.mainloop()