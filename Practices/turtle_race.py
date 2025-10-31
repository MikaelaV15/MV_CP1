#MV 1st Turtle Race 

#import all the libraries 
import turtle as t 
import random 


#create all the turtles
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()

#Make a list for the while loop later on 
turtles = [t1, t2, t3, t4, t5]

#customize each turtle 
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.setposition(20,500)
t1.pendown()


#customize each turtle 
t2.color("blue")
t2.shape("turtle")
t2.penup()
t2.setposition(20,400)
t2.pendown()


#customize each turtle 
t3.color("Purple")
t3.shape("turtle")
t3.penup()
t3.setposition(20,300)
t3.pendown()

#customize each turtle 
t4.color("green")
t4.shape("turtle")
t4.penup()
t4.setposition(20,200)
t4.pendown()


#customize each turtle 
t5.color("pink")
t5.shape("turtle")
t5.penup()
t5.setposition(20,100)
t5.pendown()

#create the finish line 
t6.color("black")
t6.shape("arrow")
t6.penup()
t6.setposition(500, 0)
t6.pendown()

#indicate where the finish line is 
t6.left(90)
t6.forward(500)

#Start the race, make it so that all the turtles move at different pixel spaces and calculate the  winner

while True: 
    for turtle in turtles:
        turtle.forward(random.randint(1,10))
    if turtle == t6:
        winner = True 
        if turtle.xcore() >= 550
            winner = {turtle}
            break 
t.write("{turtle} wins!")