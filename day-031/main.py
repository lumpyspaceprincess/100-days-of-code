import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Read from words_to_learn if it exists, else read from french_words
try:
    file = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    file = pandas.read_csv("data/french_words.csv")
to_learn = pandas.DataFrame.to_dict(file, orient="records")
current_card = {}


def next_flashcard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_flash_card)
    flip_timer = window.after(3000, func=flip_card)


# If player knew the answer, remove it from the list
def remove_then_next_flashcard():
    to_learn.remove(current_card)
    if len(to_learn) == 0:
        canvas.itemconfig(card_word, text="NO MORE WORDS!")
    listy_csv = pandas.DataFrame(to_learn)
    listy_csv.to_csv("data/words_to_learn.csv", index=False)
    next_flashcard()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_flash_card)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_flash_card = PhotoImage(file="images/card_front.png")
back_flash_card = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_flash_card)
card_title = canvas.create_text(400, 150, text=f"d", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=f"sdf", font=("Arial", 60, "bold"))
canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)


# ---------------------------- CREATE BUTTONS ------------------------------- #


# Wrong button

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_flashcard)
wrong_button.grid(column=0, row=1)

# Right button

tick_image = PhotoImage(file="images/right.png")
right_button = Button(image=tick_image, highlightthickness=0, command=remove_then_next_flashcard)
right_button.grid(column=1, row=1)


next_flashcard()

window.mainloop()
