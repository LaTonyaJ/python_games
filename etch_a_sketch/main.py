from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# direction functions
def move_forwards():
    timmy.forward(10)
    
def move_backwards():
    timmy.backward(10)

def move_clockwise():
    timmy.right(10)

def move_counter_clockwise():
    timmy.left(10)

def clear():
    timmy.home()
    timmy.pu()
    timmy.clear()
    timmy.pd()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()


