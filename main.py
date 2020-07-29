from processing import *
from tower import *
from dart import *
from enemy import *
level = "New Piskel-1.png.png"

WIDTH = 400
HEIGHT = 400
money = 100
tower_cost =20
enemyTimer = 1
time = 0
enemy_timer = 0
roundCount = 1
roundTimer = 10
roundtimer = 0
health = 30

enemies = []
towers = []
darts = []

path = [
(0, 0),
(331, 192),
(183, 396)
]
def mousePressed():
  global money
  #print(mouseX, mouseY)
  if money >= tower_cost:
    money -= tower_cost
    towers.append(Tower(mouseX, mouseY))

def setup():
  global level
  size(WIDTH, HEIGHT)
  level = loadImage(level)
  
  
def draw():
  global time, enemy_timer, roundCount, roundtimer, roundTimer
  global money, enemyTimer, health
  
  old = time
  time = millis()/1000
  delta = time - old
  
  enemy_timer += delta
  
  roundtimer += delta
  
  if enemy_timer > enemyTimer:
    enemies.append(Enemy(0, 0, path))
    enemy_timer = 0

  if roundtimer > roundTimer:
    roundCount += 1
    roundtimer = 0
    roundTimer += 5
    enemyTimer -= 0.01
  
  image(level, 0, 0, WIDTH, HEIGHT)
  for e in enemies:
    e.update()
    e.draw()
    if e.target == e.end:
      enemies.remove(e)
      health -= 1
  for t in towers:
    t.shoot(darts, enemies)
    t.draw()
  for d in darts:
    d.update()
    d.draw()
    pos = Vector2(d.x, d.y)
    for e in enemies:
      ev = Vector2(e.x, e.y)
      if pos.distanceto(ev) < e.w/2 + d.w/2:
        if d in darts:

          darts.remove(d)
          e.health-=1
          money += 1
          enemyTimer -= 0.00000001
        if e.health < 1:
          enemies.remove(e)
          money +=0
    if d.x < 0 or d.x > WIDTH or d.x < 0 or d.x > HEIGHT:
      if d in darts:
        darts.remove(d)
  fill(0, 0, 0)
  textSize(32)
  textAlign(CENTER, CENTER)
  text("money: " + str(money), width/2, height/10)
  textSize(20)
  text("round: " + str(roundCount), 200, 390)
  text("health: " + str(health), 300, 390)
  if health < 1:
    textSize(20)
    text("GAME OVER", 200, 200)
    if enemy_timer == 0:
      quit()
    if health < 0:
      health = 0
    
run()