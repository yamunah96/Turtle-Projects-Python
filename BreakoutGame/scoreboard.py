# scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-120, 50)

        self.score = 0
        self.lives=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write( f"Score: {self.score}   Lives: {self.lives}", align="center",
                   font=("Arial", 18, "bold"))

    def increase_score(self, points=10):
        self.score += points
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",
                   font=("Arial", 28, "bold"))

    def game_win(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center",
                   font=("Arial", 28, "bold"))

    def lose_life(self):
        self.lives -= 1
        self.update_score()

