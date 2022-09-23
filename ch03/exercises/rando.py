import random

number = int(input("Pick a number 1 through 10: "))
result = random.randint(1,10) 
#print(result)

for i in range(2):
  if number < result:
    number = int(input("Too low, try again: "))
  elif number > result:
    number = int(input("Too high, try again: "))
  if number == result:
    print("Correct!")
    break
      
      
      
 
  

  




  

