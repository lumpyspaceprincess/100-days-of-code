from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 30, "bold")
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    # If it's the 8th run, have a long break
    if reps % 8 == 0:
        title_label.config(text="Rest", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    # If it's another even run, have a short break
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    # If it's an odd-numbered run, do some work
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        marks = ""
        if reps % 2 != 0:
            marks += TICK
            checkmarks.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 50,), pady=10)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(103, 130, text=f"{WORK_MIN}:00", fill="white", font=FONT)
canvas.grid(column=1, row=1)

# Tick location

checkmarks = Label(text="", font=("Ariel", 24,), bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

# Start button

start_button = Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset button

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()
