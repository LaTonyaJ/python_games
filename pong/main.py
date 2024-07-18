from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)


ball = Ball()
paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=paddle1.move_up)
screen.onkey(key="Down", fun=paddle1.move_down)
screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)


game_on = True

while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    #detect collision with top and bottom of screen
    if(ball.ycor() > 260 or ball.ycor() < -260):
        ball.bounce_y()

    #detect collision with paddles
    if(ball.distance(paddle1) < 40 and ball.xcor() > 320 or ball.distance(paddle2) < 40 and ball.xcor() < -320):
        ball.bounce_x()
    
    #detect missed right paddle - game over
    if(ball.xcor() > 400):
        ball.ball_reset()
        scoreboard.increase_left()
        
    #detect missed left paddle 
    if(ball.xcor() < -400):
        ball.ball_reset()
        scoreboard.increase_right()
        
        

    

screen.exitonclick()