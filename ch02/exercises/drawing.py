import turtle

turtle.shape("turtle")

sides = int(input("How many sides do you want you shape to have? : "))

length = int(input("How long do you want each side to be? : "))

turtle.color('blue')

angle = 360/sides

for i in [angle]*sides:
  turtle.forward(length)
  turtle.left(i)

turtle.exitonclick()