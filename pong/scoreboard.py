from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Couriur", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Couriur", 80, "normal"))
        

    def increase_left(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_right(self):
        self.r_score += 1
        self.update_scoreboard()