#MV 1st 
#Import turtle 
import turtle as t 


def draw(length):
    if length > 5: 
        for i in range(3):
            turtle.forward(5)
            draw(length / 3)
            turtle.right(180)
            turtle.forward(length)
            turtle.right(60) 

turtle = t.Turtle()    
turtle.speed(3)
turtle.color("light blue")
turtle.penup()
turtle.goto(60,60)
turtle.pendown() 

for i in range(6):
    draw(100)
    turtle.right(60)

turtle.hideturtle()
t.done()