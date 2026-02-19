# main.py
import turtle
import time
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard


window = turtle.Screen()
window.setup(500, 500)
window.bgcolor("white")
window.title("Breakout Game")

# turn off automatic animation
window.tracer(0)

# OBJECTS
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

# Bricks
bricks=[]
start_x=-200
start_y=230

rows=4
cols=8

x_spacing =80
y_spacing=40
colors = ["red", "orange", "green", "blue"]
for row in range(rows):
    for col in range(cols):
        x = start_x + (col * x_spacing)
        y = start_y - (row * y_spacing)
        brick = Brick((x, y),colors[row])
        bricks.append(brick)

# KEYBOARD CONTROLS
window.listen()
window.onkeypress(paddle.start_left, "Left")
window.onkeyrelease(paddle.stop_left, "Left")

window.onkeypress(paddle.start_right, "Right")
window.onkeyrelease(paddle.stop_right, "Right")

window.onkeypress(ball.start, "space")   # start ball when SPACE is pressed

running = True

while running:
    time.sleep(0.02)  # control game speed (lower -> faster)
    
    # move ball and handle walls
    ball.move()
    ball.handle_walls(limit_x=220, limit_top=220, bottom_reset=-280)
   
    # (we will add paddle collision + bricks later)
    for brick in bricks:
        if ball.distance(brick) < 35:
            ball.bounce_y()

            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.increase_score(10)
            break

     # Paddle collision
    if ball.distance(paddle) < 60 and ball.ycor() < -220:
        print("paddle collide")
        ball.bounce_y()
        impact = ball.xcor() - paddle.xcor()
        ball.dx = impact / 8

    #  bottom hit
    if ball.ycor() < -250:
        scoreboard.lose_life()

    if scoreboard.lives >=3:
        scoreboard.game_over()
        running=False
  
    if len(bricks) == 0:
        scoreboard.game_win()
        running = False
        
    paddle.update()
    window.update()

window.mainloop()
