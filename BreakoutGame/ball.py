# ball.py
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()

        # starting position
        self.start_pos = (0, -220)
        self.goto(self.start_pos)

        # movement (velocity)
        self.dx = 4   # horizontal speed
        self.dy = 4   # vertical speed

        # how much to increase speed when bouncing off walls
        self.speed_factor = 1.05

        # ball starts idle (not moving)
        self.moving = False

    # ------------ CONTROL ------------
    def start(self):
        """Start the ball movement (called when SPACE is pressed)."""
        self.moving = True

    def stop(self):
        """Stop the ball movement."""
        self.moving = False

    # ------------ MOVEMENT ------------
    def move(self):
        """Update ball position if it is active."""
        if not self.moving:
            return

        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    # ------------ PHYSICS ------------
    def bounce_x(self):
        """Invert x direction and increase speed a bit."""
        self.dx *= -self.speed_factor

    def bounce_y(self):
        """Invert y direction and increase speed a bit."""
        self.dy *= -self.speed_factor

    def handle_walls(self, limit_x=200, limit_top=200, bottom_reset=-280):
        """
        Handle collisions with:
        - left & right walls (bounce + speed up)
        - top wall (bounce + speed up)
        - bottom: reset ball
        """

        # right wall
        if self.xcor() > limit_x:
            self.setx(limit_x)
            self.bounce_x()

        # left wall
        if self.xcor() < -limit_x:
            self.setx(-limit_x)
            self.bounce_x()

        # top wall
        if self.ycor() > limit_top:
            self.sety(limit_top)
            self.bounce_y()

        # bottom: ball lost → reset
        if self.ycor() < bottom_reset:
            self.reset_ball()

    # ------------ RESET ------------
    def reset_ball(self):
        """Reset ball position and speed, and stop it until SPACE is pressed again."""
        self.goto(0,-220)
        self.dx = 4
        self.dy = 4
        self.moving = False
