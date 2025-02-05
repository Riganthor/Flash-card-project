from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_in_language_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_immage)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_in_language_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_immage)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------------------- UI -------------------------------------------------------#

window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_immage = PhotoImage(file="C:/users/14507/PycharmProjects/Flash-card-project/images/card_front.png")
back_immage = PhotoImage(file="C:/users/14507/PycharmProjects/Flash-card-project/images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_immage)
language_text = canvas.create_text(400,150, text="Title", fill="black", font=("arial", 40, "italic"))
word_in_language_text = canvas.create_text(400, 263, text="word", fill="black", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_immage = PhotoImage(file="C:/users/14507/PycharmProjects/Flash-card-project/images/wrong.png")
wrong_button = Button(image=wrong_immage, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_immage = PhotoImage(file="C:/users/14507/PycharmProjects/Flash-card-project/images/right.png")
right_button = Button(image=right_immage, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
