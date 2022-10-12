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
  levels = int(input("Enter the number of rows:"))

  for i in range (levels, 0,-1):  
      print("*" * i)
  
rstar_pyramid()
