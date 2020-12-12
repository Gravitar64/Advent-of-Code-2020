import time

def puzzle_einlesen(datei):
  with open(datei) as f:
    return [(zeile[0],int(zeile[1:])) for zeile in f]

class Vec:
  def __init__(self, x,y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vec(self.x + other.x, self.y + other.y)      
  
  def __mul__(self, faktor):
    return Vec(self.x * faktor, self.y * faktor)

  def rot(self, grad):
    x,y = self.x, self.y
    for _ in range(grad//90):
      x,y = y,-x
    return Vec(x,y)          


def löse(p,part1):
  dirs = dict(N=Vec(0,-1), S=Vec(0,1), E=Vec(1,0), W=Vec(-1,0))
  facing = dirs['E'] if part1 else Vec(10,-1)
  pos = Vec(0,0)
  for action, value in p:
    if action in dirs:
      if part1:
        pos += dirs[action] * value
      else:
        facing += dirs[action] * value  
    elif action == 'L':
      facing = facing.rot(value)
    elif action == 'R':
      facing = facing.rot(360-value)
    elif action == 'F':
      pos += facing * value
  return abs(pos.x) + abs(pos.y)      
        


puzzle = puzzle_einlesen('Tag_12.txt')

start = time.perf_counter()
print(löse(puzzle, True),  time.perf_counter()-start)

start = time.perf_counter()
print(löse(puzzle, False),  time.perf_counter()-start)