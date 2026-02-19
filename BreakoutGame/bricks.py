# brick.py
from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position, color="blue"):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()

        # stretch turtle into rectangle
        self.shapesize(stretch_wid=1, stretch_len=2.5)

        self.goto(position)
