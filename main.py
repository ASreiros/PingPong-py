from turtle import Turtle, Screen
from paddle import Paddle
from time import sleep

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle(1)
paddle2 = Paddle(2)

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
    screen.update()
    sleep(0.1)


screen.exitonclick()
