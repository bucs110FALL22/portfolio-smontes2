import pygame
import random
import math
import time

pygame.init()
res = (400,400)
window = pygame.display.set_mode(res)
width = window.get_width()
height = window.get_height()
purpleish = (73, 58, 82)
window.fill("Gray")

def dart_board():
  pygame.draw.circle(window, purpleish, (200,200), 200)
  pygame.draw.line(window, (18, 21, 26), (200, 0), (200,400), width=2)
  pygame.draw.line(window, (18, 21, 26), (0,200), (400,200), width=2)
  pygame.display.flip()

def game():
  B = 0
  R = 0
  dart_board()

  for i in range(10):
    y = random.randrange(400)
    x = random.randrange(400)
    distance_from_center = math.hypot(x-200, y-200)
    is_in_circle = distance_from_center <= width/2
    if is_in_circle == True:
      pygame.draw.circle(window, "Red", (x,y), 5)
      R = R + 1
    elif is_in_circle == False:
      pygame.draw.circle(window, ("Black"), (x,y), 5)
      R = R - 1
    time.sleep(1)
    pygame.display.flip()
    y = random.randrange(400)
    x = random.randrange(400)
    distance_from_center = math.hypot(x-200, y-200)
    is_in_circle = distance_from_center <= width/2
    if is_in_circle == True:
      pygame.draw.circle(window, (0, 149, 255), (x,y), 5)
      B = B + 1
    elif is_in_circle == False:
      pygame.draw.circle(window, ("White"), (x,y), 5)
      B = B - 1
    time.sleep(1) 
    pygame.display.flip()

  print(B)
  print(R)

  if B < R:
    print("Red wins!")
  elif R < B:
    print("Blue wins!")
  else:
    print("Tie Game!")

pygame.display.set_caption("Start Menu");
menu = True;

blue_team = pygame.draw.rect(window,(0,0,244),(150,160,100,50));
red_team = pygame.draw.rect(window,(244,0,0),(150,230,100,50));
font = pygame.font.Font(None, 50)
text = font.render("Pick a color to begin:", True, "BLACK")
text_rect = text.get_rect(center=(width/2, height/4))
window.blit(text, text_rect)
pygame.display.flip();

while menu:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
          if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
            window.fill("Gray")
            game()
      if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 160:
        if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
          window.fill("Gray")
          game()
            
pygame.display.flip()
