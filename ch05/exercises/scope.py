#Part 1

def mult(num, var):
  result = 0
  for i in range(var):
    result = result + num

  return result

def main():
  res = mult(2,5)
  print(res)
  res = mult(4,5)
  print(res)
  res = mult(10,5)
  print(res)

main()

#Part2

def exp(num, var):
  result = 1
  for i in range(var):
    result = result * num

  return result

def main():
  res = exp(2,5)
  print(res)
  res = exp(4,5)
  print(res)
  res = exp(10,5)
  print(res)

main()

#Part 3

def square(num):
  return exp(num, 2)

def main():
  res = square(2)
  print(res)
  res = square(4)
  print(res)
  res = square(100)
  print(res)

main()