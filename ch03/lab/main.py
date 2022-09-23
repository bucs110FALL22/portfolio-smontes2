import pygame
import math
import turtle  
import random
import time

#Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

# 5. Your PART A code goes here

time.sleep(2)

michelangelo.speed(1)
leonardo.speed(1)
michelangelo.forward(random.randint(1,100))
leonardo.forward(random.randint(1,100))
time.sleep(2)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

time.sleep(1)
for i in range(10):
  michelangelo.forward(random.randint(1,10))
  leonardo.forward(random.randint(1,10))

time.sleep(2)

michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

turtle.exitonclick()

# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()

green = (0, 225, 0)
blue = (0, 0, 225)

side_length = 50
offset = 200
coords = []

#Triangle
num_sides = 3
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / (num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

window.fill(blue)
pygame.draw.polygon(window, green, coords)
pygame.display.flip()
pygame.time.delay(1500)
coords.clear()

#Square
num_sides = 4
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / (num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

window.fill(blue)
pygame.draw.polygon(window, green, coords)
pygame.display.flip()  
pygame.time.delay(2000)
coords.clear()

#Hexagon
num_sides = 6
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / (num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

window.fill(blue)
pygame.draw.polygon(window, green, coords)
pygame.display.flip()  
pygame.time.delay(2000)
coords.clear()

#Nonagon
num_sides = 9
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / (num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

window.fill(blue)
pygame.draw.polygon(window, green, coords)
pygame.display.flip()  
pygame.time.delay(2000)
coords.clear()


#Circle-ish
num_sides = 360
for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / (num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

window.fill(blue)
pygame.draw.polygon(window, green, coords)
pygame.display.flip()  
pygame.time.delay(2000)


