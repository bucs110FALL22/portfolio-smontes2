import random

number = int(input("Pick a number 1 through 10: "))

result = random.randint(1,10) 
print(result)

for i in range(2):
  if number < result:
    print("Too low!")
    number = int(input("Try again: "))
  elif number > result:
    print("Too high!")
    number = int(input("Try again: "))
  if number == result:
    print("Correct!")
    break
      
      
      
 
  

  




  

