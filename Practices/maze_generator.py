#MV 1st Maze generator 
#import turtle for the maze 
import turtle 
#import random for the walls 
import random as r 

#make variables for the grid some must have numbers 
rows = 6 
columns = 6 
cells_size = 50
boxes = []
col_grid = [[1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],]
row_grid = [[1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],
            [1,1,1,1,1,1],] 
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

    

    



#Draw the grid 
def grid_setup(boxes):
    for i in range(rows*columns):
        box = [1,1,1,1]
        boxes.append(box)

#make funtions that make the walls random
     
        


#Check that the grid is solvable 



#return the maze




#end turtle 

