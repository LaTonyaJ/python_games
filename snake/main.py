from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("green")
screen.title("Snake")
screen.setup(width=600, height=600)
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake_on_loose = True
while snake_on_loose:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if (snake.snakey[0].distance(food) < 15):
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if (snake.snakey[0].xcor() > 280 or snake.snakey[0].xcor() < -280 or snake.snakey[0].ycor() > 280 or snake.snakey[0].ycor() < -280):
        scoreboard.reset()
        snake.reset()

    if scoreboard.score > scoreboard.high_score:
        scoreboard.high_score = scoreboard.score
        with open("snake/data.txt", "w") as f:
            f.write(f"{scoreboard.high_score}")

    # detect collision with tail
    for segment in snake.snakey[1:]:
        if snake.snakey[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()