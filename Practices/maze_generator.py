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
grid_row = [[1,1,1,1,1,1,1],
            [1,0,1,0,1,0,1],
            [1,0,0,1,0,1,1],
            [1,0,1,0,0,1,1],
            [1,0,0,1,0,0,1],
            [1,1,0,1,0,0,1],]

rows = 6
grid_col = [[1,1,1,1,1,1,1],
            [1,0,0,0,1,0,1],
            [1,0,0,1,0,1,1],
            [1,0,0,0,0,1,1],
            [1,0,0,1,0,0,1],
            [1,0,0,1,0,0,1],]

columns = 6 
#how big each box is 
cells_size = 70

#set up the turtle for the grid 
t = turtle.Turtle() 
t.speed(30) 
t.color("black") 
t.pensize(3) 
t.penup() 
t.goto(-200,200) 

#Set up the actual maze 
#for loop inside of a for loop to make all the walls 
for i in range(rows):
        for j in range(columns):
                #ask if they want to make it random
                if grid_row[i][j] == 0:
                        #give it the area and the size of the space 
                        t.penup() 
                        t.forward(cells_size)
                if grid_row[i][j] == 1:
                        t.pendown()
                        t.forward(cells_size)
                        #make the turtle start again at the next row
        t.penup()
        t.goto(-200,200 - ((i+1)*cells_size)) 

t.penup() 
t.goto(-200,200)

for j in range(columns):
            if grid_col[i][j] == 0: 
                        t.penup()
                        t.forward(cells_size)
            if grid_col[i][j] == 1: 
                        t.pendown() 
                        t.forward(cells_size) 

t.penup() 
t.setheading(90)
t.back(cells_size) 
t.setheading(90)
t.pendown() 
t.forward(-280)


t.penup() 
t.goto(-200,200)

t.penup() 
t.setheading(90)
t.back(cells_size) 
t.setheading(90)
t.pendown() 
t.left(-180)


t.penup() 
t.goto(-200,200)

t.penup() 
t.setheading(90)
t.back(cells_size) 
t.setheading(90)
t.pendown() 
t.forward(-210)

t.penup() 
t.goto(10,200)

t.penup() 
t.setheading(90)
t.back(cells_size) 
t.setheading(90)
t.pendown() 
t.forward(cells_size)

t.penup() 
t.goto(80,200)

t.penup() 
t.setheading(90)
t.back(cells_size) 
t.setheading(90)
t.pendown() 
t.forward(cells_size)

t.penup() 
t.goto(85,150)

t.penup() 
t.setheading(90)
t.back(cells_size) 
t.setheading(90)
t.pendown() 
t.forward(cells_size)




t.hideturtle()
turtle.done()
