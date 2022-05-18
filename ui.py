from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.score = Label(text=f"Score: {0}", font=("Arial", 14, "normal"), fg="white", bg=THEME_COLOR, padx=20, pady=20)
        self.question = Canvas(width=300, height=350, bg="#ffffff", highlightthickness=0)
        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")
        self.true = Button(image=true, highlightthickness=0, command=self.true_pressed)
        self.false = Button(image=false, highlightthickness=0, command=self.false_pressed)
        self.question_text = None
        self.configure_ui()
        self.get_next_question()
        self.window.mainloop()

    def configure_ui(self):
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.question.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.question.create_text(150,
                                                       175,
                                                       text="kahseghfbd",
                                                       font=("Arial", 20, "italic"),
                                                       width=280)
        self.true.grid(column=0, row=2, pady=20, padx=20)
        self.false.grid(column=1, row=2, pady=20, padx=20)

    def get_next_question(self):
        self.question.config(bg="white")
        if self.quiz.still_has_questions():
            self.question.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.question.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.feedback(is_right=self.quiz.check_answer("True"))

    def false_pressed(self):
        self.feedback(is_right=self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.question.config(bg="green")
        else:
            self.question.config(bg="red")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)
