from tkinter import *
from PIL import Image, ImageTk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:  # Long break
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:  # Short break
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:  # Work session
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        marks = "✔" * math.floor(reps / 2)
        check_label.config(text=marks)


# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Arial", 20, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", font=("Arial", 20, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_label = Button(text="start", highlightthickness=0, command=start_timer)
start_label.grid(column=0, row=2)

reset_label = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_label.grid(column=2, row=2)

check_label = Label(text="", highlightthickness=0)
check_label.grid(column=1, row=3)

window.mainloop()
