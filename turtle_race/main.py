#Object State and Instances
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
screen.bgcolor("black")
results = screen.textinput(title="Wanna Bet!?"  , prompt="Enter your bet (red, orange, yellow, green, blue, purple):")
print(results)
colors = ["red", "yellow", "green", "purple", "blue", "orange"]
turtles = []
race_on = False

for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(-230, 30 * _)
    turtles.append(new_turtle)

if results:
    race_on = True
    while race_on:
        for turtle in turtles:
            turtle.fd(random.randint(0, 10))
            if(turtle.xcor() > 230):
                race_on = False
                winner = turtle.pencolor()
                if winner == results:
                    print("You Win!")
                else:
                    print(f"You Lose! The winner is {winner}!")


screen.exitonclick()