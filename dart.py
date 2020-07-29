from processing import *

class Dart:
  #creates new Dart variable
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.w = 10
    self.h = 10
    self.vx = 0
    self.vy = 0
    
  def update(self):
    self.x += self.vx
    self.y += self.vy
  def draw(self):
    ellipse(self.x, self.y, self.w, self.h)