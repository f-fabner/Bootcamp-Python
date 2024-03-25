import tkinter as tk

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"

class QuizInterface:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.true_img = tk.PhotoImage(file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_034/images/true.png")
        self.false_img = tk.PhotoImage(file="N:/Programando/ProjetosGit/Bootcamp-Python/Days/Day_034/images/false.png")
        self.score = 0
        self.score_label = tk.Label(self.window, text=f"Score: {self.score}", bg=THEME_COLOR, fg=WHITE)
        self.score_label.grid(column=1, row=0)
        
        # Quadrado branco na segunda linha e ocupando ambas as colunas com padding de 20
        padding = 20
        self.canvas = tk.Canvas(self.window, bg=WHITE, height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=padding, pady=padding)
    
        
        self.button_true = tk.Button(self.window, image=self.true_img, command=self.true_pressed, padx=20, pady=20)
        self.button_true.grid(column=0, row=2)
        
        self.button_false = tk.Button(self.window, image=self.false_img, command=self.false_pressed, padx=20, pady=20)
        self.button_false.grid(column=1, row=2)
        
        self.window.mainloop()
    
    def true_pressed(self):
        # Adicione a lógica quando o botão True é pressionado
        pass
    
    def false_pressed(self):
        # Adicione a lógica quando o botão False é pressionado
        pass
