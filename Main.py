import turtle
import time
import random


points = 0
high_Score = 0

#Windows Settings
posponer = 0.08
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#presetation
Prestentation = turtle.Turtle()
Prestentation.speed(0)
Prestentation.color("white")
Prestentation.penup()
Prestentation.hideturtle()
Prestentation.goto(0,0)
Prestentation.write("Snake classic by Ichigoon ", align= "center", font=("Courier",28,"normal"))
time.sleep(3)
Prestentation.clear()


#Player head Stetic
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("green")
player.penup()
player.goto(0,0)
player.direction = "stop"

#Player Body Stetic
seg = []

#Menu
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Points: "+str(points), align= "center", font=("Courier",25,"normal"))

#Food stetic
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)



#Funcion Moving
def up():
    player.direction = "up"
def down():
    player.direction = "down"
def left():
    player.direction = "left"
def right():
    player.direction = "right"

#Eject moving 
def mov():
    y = player.ycor()
    x = player.xcor()
    
    if player.direction == "up":
        player.sety(y + 20)

    if player.direction == "down":
        player.sety(y - 20)

    if player.direction == "left":
        player.setx(x - 20)

    if player.direction == "right":
        player.setx(x + 20)

    if  x > 280:
        player.setx(-280)

    if  x < -280:
        player.setx(280)

    if y > 280:
        player.sety(-280)
        
    if y < -280:
        player.sety(280)

#Keyboard
wn.listen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")


#Exections 
while True:
    wn.update()
    if player.distance(food) < 20:
       
       #New Position Food
       x =  random.randint(-280,280)
       y = random.randint(-280,280)
       food.goto(x,y)

       #new seg 
       body = turtle.Turtle()
       body.speed(0)
       body.shape("square")
       body.color("white")
       body.penup()
       seg.append(body)

       points = points + 1

        #High Score
       if points > high_Score:
           high_Score = points
    texto.clear()
    texto.write("Points: "+str(points)+"       High Score: "+str(high_Score), align= "center", font=("Courier",23,"normal"))
    
    #body move
    totalseg = len(seg)
    for index in range(totalseg -1, 0, -1):
        x =  seg[index - 1].xcor()
        y =  seg[index - 1].ycor()
        seg[index].goto(x,y)

    if totalseg > 0:
        x = player.xcor()
        y = player.ycor()
        seg[0].goto(x,y)

    mov()

    #game over
    for x in seg:
        if x.distance(player) < 20:
            time.sleep(1)
            player.goto(0,0)
            player.direction = "stop"

            for s in seg:
                s.goto(1000,1000)

            seg.clear()

            points = 0
            texto.clear()
            texto.write("Points: "+str(points)+"         High Score: "+str(high_Score), align= "center", font=("Courier",25,"normal"))


    time.sleep(posponer)
 