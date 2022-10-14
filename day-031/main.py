from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_flash_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_flash_card)
canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))

# Wrong button

cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# Right button

tick_image = PhotoImage(file="./images/right.png")
right_button = Button(image=tick_image, highlightthickness=0)
right_button.grid(column=1, row=1)


window.mainloop()
