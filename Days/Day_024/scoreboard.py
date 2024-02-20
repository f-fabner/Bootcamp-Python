from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Impact", 24, "bold")
FONT2 = ("Impact", 40, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("N:\Programando\ProjetosGit\Bootcamp-Python\Days\Day_024\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score =  {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("N:\Programando\ProjetosGit\Bootcamp-Python\Days\Day_024\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
