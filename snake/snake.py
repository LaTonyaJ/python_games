from turtle import Turtle


class Snake:
    def __init__(self):
        self.snakey = []
        self.create_snake()
    
    def create_snake(self):
        for _ in range(3):
            new_snake = Turtle(shape="square")
            new_snake.color("black")
            new_snake.penup()
            new_snake.goto(_ * -20, 0)
            self.snakey.append(new_snake)

    def reset(self):
        for piece in self.snakey:
            piece.goto(-1000,1000)
        self.snakey.clear()
        self.create_snake()

    def extend(self):
        self.snakey.append(Turtle(shape="square"));
        self.snakey[-1].color("black")
        self.snakey[-1].penup()
        

    def move(self):
        for seg in range(len(self.snakey) - 1, 0, -1):
            new_x = self.snakey[seg - 1].xcor()
            new_y = self.snakey[seg - 1].ycor()
            self.snakey[seg].goto(new_x, new_y)
        self.snakey[0].forward(20)

    def up(self):
        if self.snakey[0].heading() != 270:
            self.snakey[0].setheading(90)

    def down(self):
        if self.snakey[0].heading() != 90:
            self.snakey[0].setheading(270)

    def left(self):
        if self.snakey[0].heading() != 0:
            self.snakey[0].setheading(180)

    def right(self):
        if self.snakey[0].heading() != 180:
            self.snakey[0].setheading(0)