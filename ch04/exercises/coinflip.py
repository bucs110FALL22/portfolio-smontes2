import turtle
import time
import random

turtle.screensize(200, 200)
turtle.shape("turtle")
turtle.color('purple')
time.sleep(2)

run = True

while run:
  if (turtle.xcor()>199 or turtle.ycor()>199 or turtle.xcor()< -199 or turtle.ycor()< -199):
    run = False
  elif random.randint(1, 2) == 1:
    turtle.right(90)
    turtle.forward(50)
  elif random.randint(1, 2) == 2:
    turtle.left(90)
    turtle.forward(50)

print("Program ended")

turtle.exitonclick()

  

