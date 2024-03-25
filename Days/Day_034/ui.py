import tkinter as tk

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
GREEN = "#00FF00"
RED = "#FF0000"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.true_img = tk.PhotoImage(file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_034/images/true.png")
        self.false_img = tk.PhotoImage(file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_034/images/false.png")

        self.score_label = tk.Label(self.window, text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg=WHITE)
        self.score_label.grid(column=1, row=0)

        padding = 20
        self.canvas = tk.Canvas(self.window, bg=WHITE, height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=padding, pady=padding)

        self.quote_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=250, anchor="center")
        
        self.button_true = tk.Button(self.window, image=self.true_img, command=self.check_true)
        self.button_true.grid(column=0, row=2)

        self.button_false = tk.Button(self.window, image=self.false_img, command=self.check_false)
        self.button_false.grid(column=1, row=2)

        self.ask_question()

        self.window.mainloop()

    def ask_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=question_text)
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")

    def check_true(self):
        self.process_answer("True")

    def check_false(self):
        self.process_answer("False")

    def process_answer(self, user_answer):
        if self.quiz.check_answer(user_answer):
            print("You got it right!")
            self.show_feedback(GREEN)
        else:
            print("That's wrong.")
            self.show_feedback(RED)
        
        self.score_label.config(text=f"Score: {self.quiz.score}")
        
        print(f"Your current score is: {self.quiz.score}/{self.quiz.question_number}")
        print("\n")
        
        self.window.after(1000, self.reset_feedback)
        self.ask_question()

    def show_feedback(self, color):
        self.canvas.config(bg=color)

    def reset_feedback(self):
        self.canvas.config(bg=WHITE)
