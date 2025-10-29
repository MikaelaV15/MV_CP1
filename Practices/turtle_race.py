#MV 1st Turtle Race 

import turtle as t 
import random as r

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()

turtles = [t1, t2, t3, t4, t5]

t1.color("red")
t1.shape("turtle")
t1.penup()
t1.setposition(20,500)
t1.speed(r.randint(1,10))
t1.pendown()



t2.color("blue")
t2.shape("turtle")
t2.penup()
t2.setposition(20,400)
t2.speed(r.randint(1,10))
t2.pendown()



t3.color("Purple")
t3.shape("turtle")
t3.penup()
t3.setposition(20,300)
t3.speed(r.randint(1,10))
t3.pendown()


t4.color("green")
t4.shape("turtle")
t4.penup()
t4.setposition(20,200)
t4.speed(r.randint(1,10))
t4.pendown()



t5.color("pink")
t5.shape("turtle")
t5.penup()
t5.setposition(20,100)
t5.speed(r.randint(1,10))
t5.pendown()

t6.color("black")
t6.shape("arrow")
t6.penup()
t6.setposition(500,0)
t6.pendown()

t6.left(90)
t6.forward(550)


for turtle in turtles: 
    turtle.forward(400)
   