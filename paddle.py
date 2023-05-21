from turtle import Turtle

RECTANGLE_SHAPE = ((0, 0), (0, 10), (10, 10), (10, 0))


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)  # paddle is rectangle 100x20
        if position == "right":
            pos = 350
        elif position == "left":
            pos = -350
        self.goto(x=pos, y=0)
        self.speed("fastest")

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
