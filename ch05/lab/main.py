import pygame
import time

iters = {}
upper_limit = 15
scale = 20
max_val = 0
max_so_far = 0

pygame.init()
pygame.font.init()
window = pygame.display.set_mode()

def test(n):
  count = 0

  while n != 1:
    if n % 2 == 0:
      n = n / 2
      count = count + 1
    else:
      n = ((n * 3) + 1)
      count = count + 1
 
  return(count)

for i in range(2, upper_limit + 1):
  test(i)
  iters[i*scale] = test(i)*scale

  if max_so_far < test(i):
     max_val = i
     max_so_far = test(i)
  var = list(iters.items()) 
  window.fill("black")

  if len(var) >= 2:
    test1 = pygame.draw.lines(window, "white", False,  var, 2)
    new_display = pygame.transform.flip(window, False, True)
    window.blit(new_display , test1)
    pygame.display.flip()
    time.sleep(.2)

  font = pygame.font.Font(None, 25)
  text = font.render("Max so far : " + str(max_so_far), True, "White")
  window.blit(text, (10,10))
  pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False