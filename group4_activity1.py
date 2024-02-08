"""
Goal:
Programming habits that utilize Python Turtle instructions to create images are written for this task, 
which calls for a basic understanding of program mechanics, such as Program Behavior.

This file draws 3 shapes which are Hexagon, Square and a Circle
"""

import turtle



'''Size of hexagone side'''
HEXAGON_SIZE=50

'''Angle of Hexagon'''
HEXAGON_SIZE=60

'''Size of Square side'''
SQUARE_SIZE=90

'''Angle of square'''
SQUARE_ANGLE=90

'''Size of circle'''
CIRCLE_SIZE=50


'''The function (setPos) that our turtle will go to was defined here.'''
def setPos(turta,x,y): 
   turta.penup()
   turta.goto(x,y)
   turta.pendown()
   
'''Here we defined the Square function that will draw 
 the Square depending on the size you insert in line 13'''
def square(turta, square_color, border_color):  
   turta.fillcolor(square_color)               
   turta.begin_fill()
   turta.pencolor(border_color)
   turta.setheading(0)
   turta.forward(SQUARE_SIZE)
   turta.right(90)
   turta.forward(SQUARE_SIZE)
   turta.right(90)
   turta.forward(SQUARE_SIZE)
   turta.right(90)
   turta.forward(SQUARE_SIZE)
   turta.right(90)
   turta.end_fill()
 
''' Here we defined the hexagon function that will draw 
 the hexagon depending on the size you insert in line 17'''

def hexagon(turta, hexa_color, border_color): 
   turta.fillcolor(hexa_color)                
   turta.pencolor(border_color)
   turta.begin_fill()
   turta.setheading(0)
   turta.forward(HEXAGON_SIZE)
   turta.right(60)
   turta.forward(HEXAGON_SIZE)
   turta.right(60)
   turta.forward(HEXAGON_SIZE)
   turta.right(60)
   turta.forward(HEXAGON_SIZE)
   turta.right(60)
   turta.forward(HEXAGON_SIZE)
   turta.right(60)
   turta.forward(HEXAGON_SIZE)
   turta.right(60)
   turta.end_fill()


'''Here we defined the Circle function that will draw the 
 Square depending on the size you insert in line 26'''     
             
def circle(turta, circle_color, border_color):  
   turta.fillcolor(circle_color)                
   turta.pencolor(border_color)
   turta.setheading(0)
   turta.begin_fill()
   turta.circle(CIRCLE_SIZE)
   turta.end_fill()

"""The Lines below sets the position of the drawings"""
def pattern(turta, hexa_color, circle_color, square_color, border_color):
   

   # The 3 lines below are for the circle
   
   setPos(turta, -290, 230)
   circle(turta, circle_color, border_color)

   setPos(turta, -200, 80)
   circle(turta, circle_color, border_color)

   setPos(turta, -110, -70)
   circle(turta, circle_color, border_color)


   # The 3 lines below are for the hexagon
   
   setPos (turta, -130, 330)
   hexagon(turta, hexa_color, border_color)
   
   setPos (turta, -40, 180)
   hexagon(turta, hexa_color, border_color)
   
   setPos (turta, 50, 20)
   hexagon(turta, hexa_color, border_color)
   

   

   
# The 3 Lines below are for the Squares

   setPos(turta, 30, 330)
   square(turta, square_color, border_color)

   setPos(turta, 140, 180)
   square(turta, square_color, border_color)
   
   setPos(turta, 250, 20)
   square(turta, square_color, border_color)

   
'''Here below is the main function were we call it and the magic happens
 it has inputs for the following shapes that the user should input in the terminal
 and choose its colors'''

def main():
   circle_color = input("Please enter the color for Circle: ")
   hexa_color   = input("Please enter the color for Hexagon: ")
   square_color = input("Please enter the color for Square: ")
   border_color = input("Please enter the color for the Border Color: ")
   turta=turtle.Turtle()
   turta.speed(8)
 
   pattern(turta, hexa_color, circle_color, square_color, border_color)
 
   turtle.done()
 
main()