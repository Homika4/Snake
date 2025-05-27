#Turtle Graphics Game
import turtle
import math
import random
import pygame

#Set up pygame
pygame.mixer.init()


#Set up screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.bgpic("blue.png")
# wn.tracer(1)

#Draw border
my_pen = turtle.Turtle()
my_pen.up()
my_pen.setposition(-300,-300)
my_pen.pendown()
my_pen.pensize(3)
for side in range(4):
    my_pen.forward(600)
    my_pen.left(90)
my_pen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("lightblue")
player.shape("triangle")
player.penup()
player.speed(0)

#Create the score variale
score = 0

#Create goals
maxGoals = 1
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-280,280), random.randint(-280,280))

#Set up speed variable
speed = 1

def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

def is_collision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)) + math.pow(t1.ycor()-t2.ycor(),2)
    if d < 20:
        return True
    else:
        return False

#Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")

while True:
    player.forward(speed)

    #Boundary Checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        pygame.mixer.music.load("bounce.mp3")
        pygame.mixer.music.play()

    #Boundary Checking
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        pygame.mixer.music.load("bounce.mp3")
        pygame.mixer.music.play()

    # Move the goal
    for count in range(maxGoals):
        goals[count].forward(1)

        #Boundary Checking
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
            pygame.mixer.music.load("bounce.mp3")
            pygame.mixer.music.play()


        # Collision checking
        if is_collision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))
            pygame.mixer.music.load("collect.mp3")
            pygame.mixer.music.play()
            score += 1

            #Draw the score on the screen
            my_pen.undo()
            my_pen.penup()
            my_pen.hideturtle()
            my_pen.setposition(-290,310)
            score_string = f"Score: {score}"
            my_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
