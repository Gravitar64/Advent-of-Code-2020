import time


def puzzle_einlesen(datei):
  with open(datei) as f:
    return [(zeile[0], int(zeile[1:])) for zeile in f]


class Vec:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vec(self.x + other.x, self.y + other.y)

  def __mul__(self, faktor):
    return Vec(self.x * faktor, self.y * faktor)

  def rot(self, grad):
    for _ in range(grad//90):
      self.x, self.y = self.y, -self.x


def löse(p, part1=True):
  dirs = dict(N=Vec(0, -1), S=Vec(0, 1), E=Vec(1, 0), W=Vec(-1, 0))
  facing = Vec(1, 0) if part1 else Vec(10, -1)
  pos = Vec(0, 0)
  for action, value in p:
    if action in dirs:
      if part1:
        pos += dirs[action] * value
      else:
        facing += dirs[action] * value
    elif action == 'L':
      facing.rot(value)
    elif action == 'R':
      facing.rot(360-value)
    elif action == 'F':
      pos += facing * value
  return abs(pos.x) + abs(pos.y)


puzzle = puzzle_einlesen('Tag_12.txt')

start = time.perf_counter()
print(löse(puzzle),  time.perf_counter()-start)

start = time.perf_counter()
print(löse(puzzle, False),  time.perf_counter()-start)
