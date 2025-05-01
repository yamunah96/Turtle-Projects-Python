import time
import turtle
import random

gameOver=False
n_food=10
food_list=[]
screen= turtle.Screen()
screen.setup(width=1.0,height=1.0)
screen.bgcolor("khaki")

boundary= turtle.Turtle()
boundary.color("black")
boundary.speed(0)
boundary.penup()
boundary.goto(-220,220)
boundary.pendown()
boundary.pensize(2)
boundary.fillcolor("lightgreen")
boundary.begin_fill()

report= turtle.Turtle()
report.penup()
report.goto(0,0)
report.color("white")
report.hideturtle()

steps=0
pen= turtle.Turtle()
pen.penup()
pen.goto(150,120)
pen.color("red")
pen.hideturtle()


for i in range(4):
    boundary.forward(500)
    boundary.right(90)
    boundary.end_fill()
    boundary.hideturtle()

snake=turtle.Turtle()
snake.color("red")
snake.shape("square")

def move_right():
    if(snake.heading()!=180):
        snake.setheading(0.0)

def move_left():
    if(snake.heading()!=0):
        snake.setheading(180)

def move_up():
    if(snake.heading()!=270):
        snake.setheading(90)

def move_down():
    if(snake.heading()!=180):
        snake.setheading(270)

screen.listen()
screen.onkey(move_right,"Right")
screen.onkey(move_left,"Left")
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")

for i in range(n_food):
    food=turtle.Turtle()
    food.speed(0)
    food.color("blue")
    food.shape("square")
    food.penup()
    food.goto(random.randint(-220,220),random.randint(-220,220))
    food_list.append(food)
# print(len(food_list))
# print(food_list)
eaten=[False]*n_food
# print("Befor Collision: ",eaten)

#  segements - here we are storing eaten foods
segements=[]
while not gameOver:
    snake.forward(5)
    time.sleep(0.1)
    steps+=1
    pen.write(len(segements),align="center", font=("Arial",24,"bold"))

    for kk in range(n_food):
        if not eaten[kk]:
            collision= snake.distance(food_list[kk])
            if collision<20:
                food_list[kk].color("green")
                eaten[kk]=True
                segements.append(food_list[kk])
                pen.clear()

    for i in range(len(segements)-1,0,-1):
        # print(i)
        x= segements[i-1].xcor()
        y=segements[i-1].ycor()
        segements[i].goto(x,y)

    if len(segements)>0:
        x_snake= snake.xcor()
        y_snake= snake.ycor()
        segements[0].goto(x_snake,y_snake)
        
    if len(segements)==n_food:
        time.sleep(0.5)
        gameOver=True
        snake.hideturtle()
        snake.clear()
        
        for i in range(len(segements)):
            segements[i].hideturtle()
            report.write("U Won, Steps taken: "+str(steps) +"\n No of Food Eaten: "+str(len(segements))
                        ,align="center", font=("Arial",24,"bold"))
         
    if abs(snake.xcor())>260 or abs(snake.ycor())>260:
        time.sleep(0.5)
        gameOver=True
        snake.hideturtle()
        snake.clear()
        
        for i in range(len(segements)):
            segements[i].hideturtle()
        report.write("Game Over" +"\n No of Food Eaten: "+str(len(segements)),
                     align="center", font=("Arial",24,"bold"))
        
       


screen.mainloop()