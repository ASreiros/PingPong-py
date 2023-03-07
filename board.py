from turtle import Turtle, Screen


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-400, -300)
        self.pendown()
        self.color("white")
        self.width(5)
        self.draw_border()

    def draw_border(self):
        for n in range(4):
            if n % 2 == 0:
                self.pendown()
                step = 800
            else:
                self.penup()
                step = 600

            self.forward(step)
            self.left(90)
