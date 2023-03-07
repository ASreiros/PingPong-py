from turtle import Turtle, Screen
from paddle import Paddle
from board import Board
from ball import Ball
from time import sleep

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.tracer(0)
board = Board()
paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball(10)

screen.listen()
screen.onkeypress(key="Up", fun=paddle2.up)
screen.onkeypress(key="Down", fun=paddle2.down)
screen.onkeyrelease(key="Up", fun=paddle2.stop)
screen.onkeyrelease(key="Down", fun=paddle2.stop)

screen.onkeypress(key="w", fun=paddle1.up)
screen.onkeypress(key="s", fun=paddle1.down)
screen.onkeyrelease(key="w", fun=paddle1.stop)
screen.onkeyrelease(key="s", fun=paddle1.stop)

game_is_on = True
while game_is_on:
    paddle1.move_paddle()
    paddle2.move_paddle()
    ball.move_ball()
    if ball.xcor() >= 400:
        ball.start_ball(180)
    elif ball.xcor() <= -400:
        ball.start_ball(0)

    p1_bounce = False
    for segment in paddle1.segments:
        if ball.distance(segment) <= 20:
            p1_bounce = True

    p2_bounce = False
    for segment in paddle2.segments:
        if ball.distance(segment) <= 20:
            p2_bounce = True

    if p1_bounce:
        ball.bounce_right()
    elif p2_bounce:
        ball.bounce_left()

    screen.update()
    sleep(0.03)


screen.exitonclick()
