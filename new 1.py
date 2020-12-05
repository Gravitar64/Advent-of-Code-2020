import time


def puzzle_einlesen(datei):
  with open(datei) as f:
    return [x.strip() for x in f]

def löse(puzzle, dx, dy):
  px, py = 0,0
  maxX, maxY = len(puzzle[0]), len(puzzle)
  counter = 0
  while True:
    px, py = px+dx, py+dy
    if py >= maxY: return counter
    if puzzle[py][px % maxX] == '#': counter += 1


puzzle = puzzle_einlesen('Tag_03.txt')

start = time.perf_counter()
print(löse(puzzle, 3, 1), time.perf_counter()-start)

start = time.perf_counter()
lösung = 1
for dx,dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
  lösung *= löse(puzzle, dx, dy)
print(lösung, time.perf_counter()-start)
