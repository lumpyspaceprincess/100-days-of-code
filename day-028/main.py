from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Courier", 30, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
canvas.create_text(103, 130, text="00:00", fill="white", font=FONT)
canvas.grid(column=1, row=1)

# Tick location

checkmark = Label(text=TICK, font=("Ariel", 24, ), bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

# Start button

start_button = Button(text="Start", command=timer_start, bg=YELLOW)
start_button.grid(column=0, row=2)

# Reset button

reset_button = Button(text="Reset", command=timer_reset, bg=YELLOW)
reset_button.grid(column=2, row=2)



window.mainloop()