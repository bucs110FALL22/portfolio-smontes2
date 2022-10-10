#Part A

def star_pyramid():
  print("Enter the number of rows:")
  row = int(input("Rows:"))

  star = ("*")
  
  for i in range(row):
    print(star)
    star = star + "*"
  
star_pyramid()

#Part B
def rstar_pyramid():
  print("Enter the number of rows:")
  row = int(input("Rows:"))

  for i in range (0,row):  
      for j in range (row,i,-1):  
        print("*", end="")
      
      print()
  
rstar_pyramid()
