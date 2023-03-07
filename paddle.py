from turtle import Turtle
from time import sleep


class Paddle:
    def __init__(self, player):
        super().__init__()
        self.segments = []
        self.y = -40
        self.player = player
        self.x = -400
        self.create_paddle()
        self.button_pressed = False

    def create_paddle(self):
        if self.player != 1:
            self.x = 400
        for n in range(4):
            paddle_part = Turtle()
            paddle_part.penup()
            paddle_part.color("white")
            paddle_part.shape("square")
            paddle_part.turtlesize(1, 1)
            paddle_part.setheading(90)
            paddle_part.goto(self.x, self.y)
            self.y += 20
            self.segments.append(paddle_part)

    def move_paddle(self):
        for segment in self.segments:
            if self.button_pressed:
                if self.segments[-1].heading() == 90 and self.segments[-1].ycor() >= 300:
                    self.button_pressed = False
                elif segment.heading() == 270 and segment.ycor() <= -300:
                    self.button_pressed = False
                else:
                    segment.forward(10)

    def up(self):
        self.button_pressed = True
        for segment in self.segments:
            segment.setheading(90)

    def down(self):
        self.button_pressed = True
        for segment in self.segments:
            segment.setheading(270)

    def stop(self):
        self.button_pressed = False

