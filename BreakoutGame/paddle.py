from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0, -240)

        self.speed = 7
        self.boundary = 230

        self.moving_left = False
        self.moving_right = False

    # ---------------- INPUT ----------------

    def start_left(self):
        self.moving_left = True

    def stop_left(self):
        self.moving_left = False

    def start_right(self):
        self.moving_right = True

    def stop_right(self):
        self.moving_right = False

    # ---------------- UPDATE ----------------

    def update(self):
        if self.moving_left:
            new_x = self.xcor() - self.speed
            if new_x > -self.boundary:
                self.setx(new_x)

        if self.moving_right:
            new_x = self.xcor() + self.speed
            if new_x < self.boundary:
                self.setx(new_x)
