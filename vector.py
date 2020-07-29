import math

class Vector2:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    
  def length(self):
    x = self.x
    y = self.y
    return math.sqrt(x*x + y*y)
    
  def distanceto(self, other):
    x = other.x - self.x
    y = other.y - self.y
    return math.sqrt(x*x + y*y)
    
  def direction(self):
    l = self.length()
    if l  != 0:
      x = self.x / l
      y = self.y / l
      return Vector2(x, y)
    return Vector2()
