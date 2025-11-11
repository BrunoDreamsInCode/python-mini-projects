import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# --- Load data ---
try:
    data = pandas.read_csv("data/words_to_learn.csv")  # load saved progress
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")  # load original file
to_learn = data.to_dict(orient="records")
current_card = {}

# --- Functions ---
def next_card():
    """Show next random word"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancel previous timer
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(title_card, text="French", fill="black")
    canvas.itemconfig(word_card, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip_card)  # flip after 3s


def flip_card():
    """Show translation"""
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_card, text="English", fill="white")
    canvas.itemconfig(word_card, text=current_card["English"], fill="white")


def is_known():
    """Remove known word and save progress"""
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

# --- UI setup ---
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_card = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()  # show first card
window.mainloop()
