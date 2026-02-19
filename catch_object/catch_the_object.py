import turtle 
import random
import time
import csv
import os
# global variables
score=0
gamestate="menu"
aliens_group=[]
playerName=None

#----Game Timer-----
timer=10
starttime= time.time()

# screen
window= turtle.Screen()
window.bgcolor("black")
window.setup(500,500)
window.title("Random object clicking")


player= turtle.Turtle()
player.color("white")  #  both pencolor, fillcolor
# player.pencolor("red")
player.shape("arrow")
player.penup()
player.hideturtle()

score_turtle=turtle.Turtle()
score_turtle.color("white")
score_turtle.hideturtle()

timer_turtle=turtle.Turtle()
timer_turtle.color("white")
timer_turtle.hideturtle()

def update_score():
    score_turtle.clear()
    score_turtle.showturtle()
    score_turtle.write(f"Score: {score}",align="center",font=("Courier",16,"bold"))

def update_timer():
    timer_turtle.clear()
   
    timer_turtle.showturtle()
    timer_turtle.write(f"Timer: {timer}",align="center",font=("Courier",16,"bold"))

def countdown():
    global timer,gamestate
    if gamestate!="play":
        return
    timer-=1
    update_timer()

    if timer<=0:
        gameover()
        return
    window.ontimer(countdown, 1000)



csv_file="leadrboard.csv"
def create_csv():
    global csv_file
    if not os.path.exists(csv_file):
        with open(csv_file,"w",newline="") as f:
            writer= csv.writer(f)
            writer.writerow(["PlayerName","PlayerScore"])
    print("csv file Ready")

def leaderBoard():
    if not os.path.exists(csv_file):
        return 
    playerData=[]
    with open(csv_file,"r") as f:
        reader= csv.DictReader(f)
        # print(list(reader))   
        #[{'PlayerName': 'Yamuna', 'Score': '100'}, {'PlayerName': 'Angad', 'Score': '200'}]
        for row in reader:
            playerData.append(row)
        return playerData

def update_player_data(PlayerName, PlayerScore):
    # check the playname already exist Yamuna - 100 (game 1)
    # Yamuna - 120 (game 2)   (in this condtion we need replace the score only by comapring)
    # if the player name not exist create a new one

    found=False
    playerData= leaderBoard()
    for i in playerData:
        '''
        {'PlayerName': 'Yamuna', 'Score': '100'}
        {'PlayerName': 'Angad', 'Score': '200'}
        '''
        if i['PlayerName'] == PlayerName:
            found=True
            if PlayerScore > int(i['PlayerScore']) :
                i["PlayerScore"]=PlayerScore
                playerData.remove(i)
                playerData.append({'PlayerName': PlayerName, 'PlayerScore': PlayerScore})
                print(f"{PlayerName} LeadBoard { PlayerScore} Updated")
                print("whats player Data: ",playerData)
            break

    if not found:
        playerData.append([{'PlayerName': PlayerName, 'PlayerScore': PlayerScore}])
        print("whats player Data: ",playerData)

    with open(csv_file,"w",newline="") as f:
            writer= csv.writer(f)
            writer.writerow(["PlayerName","PlayerScore"])
            for i in playerData:
                print("i value",i)
                writer.writerow([i["PlayerName"],i["PlayerScore"]])
            print("LeaderBoard Updated")


# player.showturtle(), hideturtle()
# objects
def create_aliens():
    global aliens_group
    colors=["red","green","blue","orange","purple"]
    for i in range(5):
        alien= turtle.Turtle()
        alien.speed(0)
        alien.shape("turtle")
        alien.color(random.choice(colors))
        alien.penup()
        alien.goto(random.randint(-230,230),random.randint(-230,230))
        aliens_group.append(alien)

def move_left():
    global gamestate
    if gamestate == "play":
        if player.heading()!=180:
            player.setheading(180)
        x=player.xcor()
        x-=20
        player.setx(x)
        # print("check x",x)
        if x <= -240:
            player.setx(-240)
    else:
        return

def move_right():
    if gamestate == "play":
        if player.heading()!= 0:
            player.setheading(0)
        x=player.xcor()
        x+=20
        player.setx(x)
        # print("check x",x)
        if x >= 240:
            player.setx(240)
    else:
        return

def move_down():
    if gamestate == "play":
        if player.heading()!=270:
            player.setheading(270)
        y=player.ycor()
        y-=20
        player.sety(y)
        # print("check x",y)
        if y <= -240:
            player.sety(240)
    else:
        return

def move_up():
    if gamestate == "play":
        if player.heading()!=90:
            player.setheading(90)
        y=player.ycor()
        y+=20
        player.sety(y)
        # print("check x",y)
        if y >=240:
            player.sety(240)
    else:
        return

def move_aliens():
    if gamestate !="play":
        return
    
    for alien in aliens_group:
        alien.goto(random.randint(-230,230),random.randint(-230,230))   
    window.ontimer(move_aliens,4000)    

def destory():
    global score, gamestate
    if gamestate == "play":
        for alien in aliens_group:
            # print(alien.color()[0])
            # sprite.distance(target)
            distance= player.distance(alien)
            # print(distance)
            if distance<=30:
                print(f"{alien.color()[0]} is destoryed with the distane {distance}")
                score+=1
                update_score()
                alien.hideturtle()
                aliens_group.remove(alien)
            
def check_collision_loop():
    destory()
    window.ontimer(check_collision_loop,100)


msg= turtle.Turtle()
msg.color("white")
msg.penup()
msg.goto(100,100)


#  Game Lopp machines
def game_loop():
    global gamestate

    if gamestate == "play":
        check_collision_loop()

    window.ontimer(game_loop,100)

# ----------------------------------Menu--------------------------------------------
def show_menu():
    global gamestate,score,timer
    gamestate="menu"
    score=0
    timer=10

    msg.clear()
    window.bgcolor("purple")

    msg.goto(0,80)
    msg.write(f" Welcome To Alien Invansion Game\n 1.Instructions\n 2.Start Game\n3.View Dashboard\n4.ExitGame",
              font=("Arial",10,"bold"),align="center")

def instructions():
    print("instructions")
    global gamestate
    gamestate="instructions"

    msg.clear()
    window.bgcolor("orange")
    msg.write(f"Move the arrow keys, touch aliens to score, complete the game within timer",
                font=("Arial",10,"bold"),align="center")
    

def start_game():
    print("game")
    global gamestate,score,timer,playerName
    gamestate="play"
    playerName= window.textinput("PlayerName","Enter Your Name: ")
    print(playerName)
    create_csv()   # lets create csv_file
    window.listen()
    
    msg.clear()
    window.bgcolor("black")

    player.goto(0,-150)
    player.showturtle()

    score_turtle.penup()
    timer_turtle.penup()
    score_turtle.goto(-180,150)
    timer_turtle.goto(180,150)
    score_turtle.hideturtle()
    timer_turtle.hideturtle()

    create_aliens()
    countdown()
    update_score()
    update_timer()
    move_aliens()
    

def dashboard():
    print("dashboard")

def gameover():
    global gamestate
    gamestate="gameover"

    end_pen = turtle.Turtle()
    end_pen.hideturtle()
    end_pen.color("red")
    end_pen.penup()
    end_pen.goto(0, 0)
    end_pen.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
    player.hideturtle()
    for alien in aliens_group:
        alien.hideturtle()


# Game states== menu,start,over
window.listen()

window.onkeypress(instructions, '1')
window.onkeypress(start_game, '2')
window.onkeypress(dashboard, '3')
window.onkeypress(show_menu, "m")
window.onkeypress(window.bye, '4')


window.onkeypress(move_left,"Left")
window.onkeypress(move_right,"Right")
window.onkeypress(move_up,"Up")
window.onkeypress(move_down,"Down")

#  main functions
show_menu()
game_loop()
update_player_data("Angad",250)
window.mainloop()
