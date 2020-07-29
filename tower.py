from processing import *
from dart import *
from vector import *
class Tower:
  #creates new Tower variable
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 20
    self.h = 20
    self.timer = 0
    self.firespeed = 1
    self.distance = 120
    
  def shoot(self, darts, enemies):
    self.timer += 1/60
    if self.timer > self.firespeed:
      self.timer = 0
      enemy = None
      pos = Vector2(self.x, self.y)
      dist = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999
      for e in enemies:
        ev = Vector2(e.x, e.y)
        d = pos.distanceto(ev)
        if d<self.distance:
          if d < dist:
            dist = d
            enemy = e
      if enemy != None:
        
        vx = enemy.x - pos.x
        vy = enemy.y - pos.y
        vel = Vector2(vx, vy).direction()
        dart = Dart(self.x, self.y)
        dart.vx = vel.x * 20
        dart.vy = vel.y * 20
        darts.append(dart)
      
  def draw(self):
    fill(0, 255, 255)
    ellipse(self.x, self.y, self.w, self.h)