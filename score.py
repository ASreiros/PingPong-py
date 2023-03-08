from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.p1_score = 0
        self.p2_score = 0
        self.draw_score()

    def dots(self):
        self.goto(0, 305)
        self.write(f":", move=False, align='center', font=('Arial', 50, 'normal'))

    def draw_score(self):
        self.clear()
        self.dots()
        self.goto(-40, 300)
        self.write(f"{self.p1_score}", move=False, align='center', font=('Arial', 50, 'normal'))
        self.goto(40, 300)
        self.write(f"{self.p2_score}", move=False, align='center', font=('Arial', 50, 'normal'))

    def add_score_p1(self):
        self.p1_score += 1
        self.draw_score()

    def add_score_p2(self):
        self.p2_score += 1
        self.draw_score()
