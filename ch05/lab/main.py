import pygame

iters = {}
upper_limit = 40
scale = 20

pygame.init()
pygame.font.init()
window = pygame.display.set_mode()

def test(n):

  count = 0
  max_so_far = 0
  
  while n != 1:
    if n % 2 == 0:
      n = n / 2
      count = count + 1
    else:
      n = ((n * 3) + 1)
      count = count + 1
    max_so_far = max_so_far + 1  
 
  return(count)

for i in range(2, upper_limit + 1):
  test(i)
  iters[i*scale] = test(i)*scale

max_val = test(i)
print(max_val)
  
var = list(iters.items()) 

test = pygame.draw.lines(window, "white", False,  var, 5)
new_display = pygame.transform.flip(window, False, True)
window.blit(new_display , test)
pygame.display.flip()


# font = pygame.font.Font(None, 50)
# text = font.render("Pick a color to begin:", True, "White")
# text_rect = text.get_rect()
# window.blit(text, text_rect)

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False