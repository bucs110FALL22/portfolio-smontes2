class Player:
  def __init__(self, pnum):
    self.color = "red"
    self.number_of_deaths = 0 
    self.luigi = False

class Enemy:
  def __init__(self, num):
    self.x = 0 #Starting position 
    self.y = 0 
    self.full_life = True
    self.speed = 3

class Lucky_Block:
  def __init__(self):
    self.powerup = False #Is block being touched on start
    self.color = "yellow"
    self.prize = 10
    