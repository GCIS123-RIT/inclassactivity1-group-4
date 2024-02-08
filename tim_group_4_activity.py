"""This code illustrates three geometric figures: hexagon, square, circle. The idea is to create a drawing of these three types of figures in different color chosen by the user."""

import turtle

'''Size of one side of the hexagon figure'''
HEXAGON_SIZE=50

'''Size of one side of the square figure'''
SQUARE_SIZE=90

'''Size of one side of the circle figure'''
CIRCLE_SIZE=50

'''In this line the "Set Position" function is defined which determines where the Turtle module shall move to.'''

def setPos(turta,x,y): 
   turta.penup()
   turta.goto(x,y)
   turta.pendown()

'''In this line below the "hexagon" function is defined.'''

def hexagon(turta, hexa_color, border_color): 
   turta.fillcolor(hexa_color)                
   turta.pencolor(border_color)
   turta.begin_fill()
   turta.setheading(0)
   turta.forward(HEXAGON_SIZE)                # The hexagon size is determined by the value of HEXAGON_SIZE.
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

'''In this line below the "square" function is defined.'''
   
def square(turta, square_color, border_color): 
   turta.fillcolor(square_color)               
   turta.pencolor(border_color)
   turta.begin_fill()
   turta.setheading(0)
   turta.forward(SQUARE_SIZE)               # The square size is determined by the value of SQUARE_SIZE.
   turta.right(90)
   turta.forward(SQUARE_SIZE)
   turta.right(90)
   turta.forward(SQUARE_SIZE)
   turta.right(90)
   turta.forward(SQUARE_SIZE)
   turta.end_fill()
 
'''In this line below the "circle" function is defined.'''

def circle(turta, circle_color, border_color): 
   turta.fillcolor(circle_color)               
   turta.pencolor(border_color)
   turta.setheading(0)
   turta.begin_fill()
   turta.circle(CIRCLE_SIZE)                   # The circle size is determined by the value of CIRCLE_SIZE.          
   turta.end_fill()

"""In the lines below the "Pattern" function is defined determining the steps of the process of drawing."""
def pattern(turta, hexa_color, circle_color, square_color, border_color):
   
   """In the lines below, the position and parameters for the hexagon figure are outlined"""
   
   setPos (turta, -130, 330)
   hexagon(turta, hexa_color, border_color)
   
   setPos (turta, -40, 180)
   hexagon(turta, hexa_color, border_color)
   
   setPos (turta, 50, 20)
   hexagon(turta, hexa_color, border_color)

    """In the lines below, the position and parameters for the square figure are outlined"""

   setPos(turta, 30, 330)
   square(turta, square_color, border_color)

   setPos(turta, 140, 180)
   square(turta, square_color, border_color)
   
   setPos(turta, 250, 20)
   square(turta, square_color, border_color)

   """In the lines below, the position and parameters for the circle figure are outlined"""
   
   setPos(turta, -290, 230)
   circle(turta, circle_color, border_color)

   setPos(turta, -200, 80)
   circle(turta, circle_color, border_color)

   setPos(turta, -110, -70)
   circle(turta, circle_color, border_color)
   
"""In the lines below the "main" function is defined unifying all the above functions to carry out the full operation."""

def main():
   hexa_color   = input("In this line enter the color for Hexagon: ")
   circle_color = input("In this line enter the color for Circle: ")
   square_color = input("In this line enter the color for Square: ")
   border_color = input("In this line enter the color for the Border Color: ")
   turta=turtle.Turtle()
   turta.speed(20)
 
   pattern(turta, hexa_color, square_color, circle_color, border_color)
 
   turtle.done()
 
main()
