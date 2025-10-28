# MV 1st Libraries and built in functions 
import turtle as t
import random 
color= ["orange", "green", "blue", "purple", "red"]
side = random.randint(10,500)
t.color(random.choice(color))
t.shape("turtle")

t.fillcolor(random.choice(color))
t.begin_fill()
for x in range(1,4):
    t.forward(side)
    t.right(90)
t.end_fill()

t.penup()
t.goto(50,50)

t.pendown()

t.fillcolor(random.choice(color))
t.begin_fill()
for x in range(1,4):
    t.forward(side)
    t.right(90)
t.end_fill()


t.done()