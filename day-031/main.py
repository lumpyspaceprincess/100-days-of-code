import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- READ WORD LIST ------------------------------- #


file = pandas.read_csv("data/french_words.csv")
data = pandas.DataFrame.to_dict(file, orient="records")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_flash_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_flash_card)
canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)


# ---------------------------- CREATE NEW FLASHCARDS ------------------------------- #


def word_language(language):
    canvas.delete("all")
    canvas.create_image(400, 263, image=front_flash_card)
    canvas.create_text(400, 150, text=f"{language}", font=("Arial", 40, "italic"))


def word_text(text):
    canvas.create_text(400, 263, text=f"{text}", font=("Arial", 60, "bold"))


def next_flashcard():
    language = "French"
    new_word = random.choice(data)
    text = new_word["French"]
    word_language(language)
    word_text(text)


# ---------------------------- CREATE BUTTONS ------------------------------- #


# Wrong button

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_flashcard)
wrong_button.grid(column=0, row=1)

# Right button

tick_image = PhotoImage(file="images/right.png")
right_button = Button(image=tick_image, highlightthickness=0, command=next_flashcard)
right_button.grid(column=1, row=1)


next_flashcard()

window.mainloop()
