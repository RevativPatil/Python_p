import turtle
import random #
import time #Make the snake move faster after eating food
delay = 0.1 #when delay value is less speed increase
sc = 0 #score
hs= 0 #highest score

#creadting a body snake
bodies=[]

#creating a screen
s1=turtle.Screen()
s1.title("Snake game")
s1.bgcolor("light blue")
s1.setup(width=600,height=600)

#creating a head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.fillcolor("black")
head.penup()                           #penup and pendown function when you don't want to draw the line when it changes the position
head.goto(0,0)        #for starting it from beginning whenever the game starts new
head.direction="stop"

#creating food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.penup()
food.ht()                #hide turtle
food.goto(250,200)         #move the food 
food.st()                  #show turtle
food.direction="stop"

#Scoreboard
score=turtle.Turtle()
score.ht()                  #kuch dikhe na our dikhe to shape ke format mai na dikhe text ke format mai dikhe
score.penup()
score.goto(-250,250)
score.write("score:0 | Highest Score:0")







turtle.done()
