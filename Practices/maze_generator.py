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
rows = 6 
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
    for j in range(colums):
        #randomly make the walls 
        if r.randint([True,False]):
            #give it the area and the size of the space 
            t.goto(-200 + j * cell_size, 200 + i * cell_size)
            t.pendown() 
            t.forward(cell_size)
            t.penup() 
            #make the turtle start again at the next row
        t.goto(-200,200 * cell_size) 




t.hideturtle()

turtle.done()
