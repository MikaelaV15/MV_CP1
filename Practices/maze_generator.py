#MV 1st Maze generator 
#import turtle for the maze 
import turtle 
#import random for the walls 
import random as r 

#make variables for the grid some must have numbers 

rows = 6 
columns = 6 
cells_size = 30 
row_grid = []
col_grid = [] 
walls = [] 
visit = []

back = "Maze Generator"
pencolor = ("black")
t = turtle.Pen()
t.speed(0)
t.hideturtle()

#set up the turtle for the grid 
def turtle_setup():
    turtle.title("forgotten")
    turtle.hideturtle
    turtle.speed(5)
    turtle.pensize(4)
    turtle.penup

#Set up the grid 
def setup():
    back = turtle.Screen()
    back.bgcolor("black") 
    back.title("Maze Generator") 
    return back 
    

#Draw one of the walls 
def walls():
  turtle.penup() 
  turtle.goto() 
  turtle.pendown() 
  turtle.begin_fill()
  for i in range(4):
        turtle.forward(cells_size) 
        turtle.right(90) 
turtle.end_fill()



#Draw the grid 
def grid_setup(boxes):
    for i in range(rows*columns):
        box = [1,1,1,1]
        boxes.append(boxes) 


turtle.done()