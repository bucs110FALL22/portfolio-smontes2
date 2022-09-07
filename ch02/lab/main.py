import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 14

cost_per_class = (cost_per_week / classes_per_week)

print("Here is your cost per class:" , cost_per_class , ", have a nice day! ")

print(weeks , type(weeks))
print(classes , type(classes))
print(tuition , type(tuition))
print(cost_per_week , type(cost_per_week))
print(classes_per_week , type(classes_per_week))
print(cost_per_class , type(cost_per_class))


#Part B

mySports = ["Baseball" , "Track" ,  "Swimming" , "Football" , "Hockey"]

mySportsRandom = random.choice(mySports)

print(mySportsRandom)


