import turtle

turtle.shape("turtle")
turtle.color('purple')
turtle.delay(10)
square = 4
length = 50
angle = 90

for i in [angle]*square:
  turtle.forward(length)
  turtle.left(i)
  
turtle.penup()
turtle.setpos(100,100)

turtle.color('red')
turtle.pendown()

for k in [angle]*square:
  turtle.forward(length)
  turtle.left(k)

turtle.exitonclick()