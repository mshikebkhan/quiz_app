from tkinter import *
from quiz_brain import QuizBrain
from data_builder import build_question_data

THEME_COLOR = "#b0dcc4"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window setup.
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(background=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        # Heading.
        self.heading = Label(font=("Bahnschrift", 15), text="Quizzler")
        self.heading.config(background=THEME_COLOR)
        self.heading.grid(column=0, row=0)

        # Score label
        self.score = Label(font=("Bahnschrift", 15), text="Score: 0")
        self.score.config(background=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # Canvas setup.
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_rectangle(0, 0, 300, 250, outline="black", width=2, fill='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=290,
            text="Question is here.",
            font=("Bahnschrift", 15, "italic")
        )
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # Buttons.
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, background=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, background=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        reset_img = PhotoImage(file="images/reset.png")
        self.reset_button = Button(image=reset_img, background="white", highlightthickness=0,
                                   command=self.reset_quiz)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score.config(fg="black")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="")
            self.reset_button.grid(column=0, row=1, columnspan=2)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        correct = self.quiz.check_answer("True")
        if correct:
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.score.config(fg="red")
        self.window.after(1000, self.get_next_question)

    def false_pressed(self):
        correct = self.quiz.check_answer("False")
        if not correct:
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.score.config(fg="red")
        self.window.after(1000, self.get_next_question)

    def reset_quiz(self):
        self.quiz.score = 0
        self.score.config(text="Score: 0")
        self.reset_button.grid_forget()
        self.quiz.question_list = build_question_data()
        self.quiz.question_number = 0
        self.get_next_question()
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

