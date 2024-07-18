from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.penup()
        self.goto(x,y)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 250:
            self.setpos(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -250:
            self.setpos(x=self.xcor(), y=new_y)