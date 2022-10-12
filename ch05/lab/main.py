import random

n = random.randrange(1, 101, 1)

while n > 1:
 for i in range(n):
   if n % 2 == 0:
     n = n / 2
     print(n)
   elif n % 3 == 1:
     n = n * 3 + 1
     print(n)
