def percentage_to_letter(score=0):

  score = float(input("Enter a grade: "))
  
  if score >= 90:
    return("A")
  elif score >= 80 and score < 90:
    return("B")
  elif score >= 70 and score < 80:
    return("C")
  elif score >= 60 and score < 70:
    return("D")
  elif score < 60:
    return("F")

def is_passing(letter=None):
  if letter in "ABC":
    return("True")
  elif letter in "DF":
    return("False")

grade = percentage_to_letter()
print("Letter grade: " + grade)

pf = is_passing(grade)
print("Pass: " + pf)





