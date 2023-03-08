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

        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for m in range(30):
            if m % 2 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(20)

    def game_over(self, p):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=('Arial', 50, 'normal'))
        self.goto(0, -50)
        self.write(f"Player {p}     won.", move=False, align='center', font=('Arial', 20, 'normal'))