from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.75, .75, 1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.refresh()
        self.showturtle()

    def refresh(self):
        new_x = random.randint(-260, 260)
        new_y = random.randint(-260, 260)
        self.goto(new_x, new_y)

    

