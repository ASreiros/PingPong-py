from turtle import Turtle
from random import randint

TIMER = 10


class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed = speed
        self.timer = 0

        if randint(0, 1) > 0:
            self.trow = 0 + randint(-60, 60)
        else:
            self.trow = 180 + randint(-60, 60)
        self.start_ball(self.trow)

    def start_ball(self, p):
        self.goto(0, 0)
        r = randint(-10, 10)
        self.setheading(p + r)
        self.timer = TIMER

    def move_ball(self):
        if self.timer == 0:
            for n in range(self.speed):
                self.forward(1)
                height = self.ycor()
                if height > 290:
                    heading = self.heading()
                    if 90 > heading > 0:
                        self.setheading(360-heading)
                    else:
                        angle = 180 - heading
                        self.setheading(180+angle)
                elif height < -290:
                    heading = self.heading()
                    if 360 > heading > 270:
                        angle = 360 - heading
                        self.setheading(angle)
                    else:
                        angle = 270 - heading
                        self.setheading(90+angle)
        else:
            self.timer -= 1

    def bounce_left(self):
        heading = self.heading()
        r = randint(-30, 30)
        if 90 > heading >= 0:
            self.setheading(180 - heading + r)
        else:
            angle = 360 - heading
            self.setheading(180 + angle + r)

    def bounce_right(self):
        heading = self.heading()
        r = randint(-30, 30)
        if 180 >= heading > 90:
            angle = 180 - heading
            self.setheading(angle + r)
        else:
            angle = heading - 180
            self.setheading(360 - angle + r)
