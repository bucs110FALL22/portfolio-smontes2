import turtle
import time

def drawEqShape(myturtle=None, num_sides=0, side_length=0):
    if myturtle:
      for i in range(num_sides):
        myturtle.forward(side_length)
        myturtle.left(360/num_sides)
      time.sleep(2)
  
leo = turtle.Turtle()
num_sides = int(input("Number of sides:"))
side_length = int(input("Length of sides:"))

drawEqShape(leo, num_sides, side_length)

turtle.exitonclick()