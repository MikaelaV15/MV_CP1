#MV 1st Maze generator 
#import turtle for the maze 
import turtle 
#import random for the walls 
import random as r 

#make variables for the grid some must have numbers 
back = setup() 
pencolor = ("black")
pen.speed(0)
pen.hideturtle() 


rows = 6 
columns = 6 
cells_size = 30 
walls = [] 
visit = []



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
                        turtle.forward() 
                        turtle.right(90) 
            turtle.endfill 



#Draw the grid 
def grid_setup(boxes):
    for i in range(rows*columns):
        box = [1,1,1,1]
        boxes.append(box)

#make funtions that make the walls random
     
        


#Check that the grid is solvable 



#return the maze




#end turtle 

