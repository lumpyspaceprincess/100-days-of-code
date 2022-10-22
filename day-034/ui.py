import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        # Create score UI

        self.score = Label(text=f"Score: {self.quiz.score}", fg="white", background=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # Create canvas for questions

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=260,
            text="quote goes here",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Create buttons

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image)
        self.true_button.grid(column=0, row=2)
        self.true_button.config(highlightthickness=0, background=THEME_COLOR, command=self.clicked_true)

        self.false_button = Button(image=false_image)
        self.false_button.grid(column=1, row=2, )
        self.false_button.config(highlightthickness=0, background=THEME_COLOR, command=self.clicked_false)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions() is True:
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(command="")
            self.false_button.config(command="")

    def clicked_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def clicked_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct: bool):
        if is_correct is True:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
