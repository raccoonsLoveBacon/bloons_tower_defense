from processing import *
from vector import *

class Enemy:
  #creates new Tower variable
  def __init__(self, x, y, path):
    self.path = path
    self.healthup = 2
    self.x = path[0][0]
    self.y = path[0][1]
    self.target = 1
    self.end = len(path)
    self.w = 20
    self.h = 20
    self.health = int(random(1, self.healthup))
    self.healthmax = self.health
    self.speed = 1.99
    self.dead = False
    
    
  def update(self):
    nextPoint = self.path[self.target]
    nextPoint = Vector2(nextPoint[0], nextPoint[1])
    pos = Vector2(self.x, self.y)
    
    if pos.distanceto(nextPoint) > self.speed:
      newx = nextPoint.x - pos.x
      newy = nextPoint.y - pos.y
      direction = Vector2(newx, newy).direction()
      self.x += direction.x * self.speed
      self.y += direction.y * self.speed
    else:
      if self.target < self.end :
        self.target += 1
  def draw(self):
    if self.health == 1:
      fill(255, 0, 0)
    else:
      fill(255, 0, 0)
    ellipse(self.x, self.y, self.w, self.h)
    rect(self.x - self.w/2, self.y - (self.h / 2) - 10, (self.health/self.healthmax) * self.w, 2)