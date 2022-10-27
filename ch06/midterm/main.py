import turtle

t = turtle.Turtle()
turtle.screensize(500,500)
t.penup()
t.goto(0,50)
t.pendown()

def main():
  var = head()
  shirt(color)
  arms()
  legs()
  shoes()
  t.penup()
  t.goto(10,75)
  t.pendown()
  var2 = eyes()
  t.penup()
  t.goto(30,75)
  t.pendown()
  eyes()
  t.penup()
  t.goto(15,70)
  t.pendown()
  mouth()
  t.hideturtle()
  print("Halloween Steves head has " + str(var) + " sides and his eyes are " + var2 + ".")

def head(lines=0):
  t.fillcolor("#ff7518")
  t.begin_fill()
  for i in range(4):
    t.forward(50)
    t.left(90)
    lines = lines + 1
  t.end_fill()
  pos = t.pos()
  print(pos)
  return(lines)

def shirt(color):
  t.fillcolor(color)
  t.right(90)
  t.begin_fill()
  for i in range(2):
    t.forward(80)
    t.left(90)
    t.forward(50)
    t.left(90)
  t.right(90)
  for i in range(4):
    t.forward(20)
    t.left(90)
  t.goto(50,50)
  for i in range(4):
    t.left(90)
    t.forward(20)
  t.end_fill()
  t.penup()
  t.goto(-20,30)
  
def eyes(eye_color= "black"):
  t.fillcolor("black")
  t.begin_fill()
  for i in range(4):
    t.forward(10)
    t.left(90)
  t.end_fill()
  return(eye_color)

def mouth():
  t.fillcolor("black")
  t.begin_fill()
  for i in range(2):
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
  t.end_fill()

def arms():
  t.fillcolor("#a97d64")
  t.begin_fill()
  for i in range(2):
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(20)
  t.penup()
  t.goto(50,30)
  t.pendown()
  for j in range(2):
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(20)
  t.end_fill()

def legs():
  t.penup()
  t.goto(0,-30)
  t.pendown()
  t.fillcolor	("#494697")
  t.begin_fill()
  for i in range(2):
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(25)
  t.left(180)
  t.forward(50)
  for j in range(2):
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(25)
  t.end_fill()
  t.goto(50,-100)

def shoes():
  t.fillcolor("#6b6b6b")
  t.begin_fill()
  for i in range(2):
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(25)
  t.goto(25,-100)
  for j in range(2):
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(25)
  t.end_fill()

color = input(str("What color do you want steves shirt to be? : "))
main()

turtle.exitonclick()