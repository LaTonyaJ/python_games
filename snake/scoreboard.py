from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("snake/data.txt") as f:
            self.high_score = int(f.read())
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", font=('Arial', 18, 'bold'), align="center")
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", font=('Arial', 18, 'bold'), align="center")

    def reset(self):
        self.clear()
        self.score = 0
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", font=('Arial', 18, 'bold'), align="center")



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over!", font=('Arial', 24, 'bold'), align="center")

