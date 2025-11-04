#MV 1st Maze generator 
#import turtle and random 
import turtle as t 
import random as r
#set the proportions (width and height of the maze)
#Set the height to 400 
height = 400
#set the width to 400 
width = 400 
#make the grid coordinates for a 6 by 6
#make the row grid   
row_grid = t.Turtle()
column_grid = t.Turtle()
row_grid = [[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)],
           [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)],
           [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5)],
           [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5)],
           [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5)],
           [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)]]


#make the colimn grid 
column_grid = [[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)],
           [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)],
           [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5)],
           [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5)],
           [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5)],
           [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)]]

