import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Store quiz logic instance
        self.quiz = quiz_brain

        # Main window settings
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        # Question display canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.button_true
        )
        self.true_button.grid(row=2, column=0)

        # False button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.button_false
        )
        self.false_button.grid(row=2, column=1)

        # Show the first question
        self.get_next_question()

        # Start the UI loop
        self.window.mainloop()

    def get_next_question(self):
        """Load the next question on the screen."""
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # End of quiz message
            self.canvas.itemconfig(self.question_text, text="You reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def button_true(self):
        """Handle click on the TRUE button."""
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def button_false(self):
        """Handle click on the FALSE button."""
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Show feedback color and load next question after delay."""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # After 1 second, load the next question
        self.window.after(1000, self.get_next_question)
