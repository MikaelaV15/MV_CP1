#MV 1st Maze generator 
#import turtle for the maze 
import turtle 
#import random for the walls 
import random as r 
# set up the screen 
screen = turtle.Screen() 
screen.bgcolor("white")
screen.title("Maze Generator")


#make variables for the grid some must have numbers 
#number of rows and colums 
grid_row = [[(0,0), (0,1),(0,2), (0,3), (0,4), (0,5)],
        [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5)],
        [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5)],
        [(3,0), (3,1), (3,2), (3,3), (3,4), (3,5)],
        [(4,0), (4,1), (4,2), (4,3), (4,4), (4,5)],
        [(5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]]
rows = 6
grid_col = [[(0,0), (0,1),(0,2), (0,3), (0,4), (0,5)]
        [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5)],
        [(2,0), (2,1), (2,2), (2,3), (2,4), (2,5)],
        [(3,0), (3,1), (3,2), (3,3), (3,4), (3,5)],
        [(4,0), (4,1), (4,2), (4,3), (4,4), (4,5)],
        [(5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]]
columns = 6 
#how big each box is 
cells_size = 30 

#set up the turtle for the grid 
t = turtle.Turtle() 
t.speed(0) 
t.color("black") 
t.pensize(5) 
t.penup() 
t.goto(-200,200) 
#Set up the actual maze 
#for loop inside of a for loop to make all the walls 
for i in range(rows):
    for j in range(columns):
        #ask if they want to make it random
        
            #give it the area and the size of the space 
            t.goto(-200 + j * cells_size, 200 + i * cells_size)
            t.pendown() 
            t.forward(cells_size)
            t.penup() 
        
            t.goto(-200 + j * cells_size, 200 + i * cells_size)
            t.penup()
            t.forward(cells_size)
            t.pendown()
            #make the turtle start again at the next row
            t.goto(-200,200 - i  * cells_size) 




t.hideturtle()

turtle.done()
