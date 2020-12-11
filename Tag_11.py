import time


def puzzle_einlesen(datei):
  with open(datei) as f:
    return {(x,y):0  for y,zeile in enumerate(f) for x,char in enumerate(zeile) if char == 'L'}

def occ_neighbors(map,x,y,see):
  count = 0
  for dx, dy in ((-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)):
    x2, y2 = x, y
    while True:
      x2 += dx; y2 += dy
      if (x2,y2) in map and map[(x2,y2)] == 0: break
      if (x2,y2) in map and map[(x2,y2)] == 1:
        count += 1
        break
      if see == 1: break
      if x2 < 0 or x2 >95 or y2 < 0 or y2 > 98: break
  return count    

def löse(map,see,toleranz):
  occ1 = 0
  while True:
    map2 = map.copy()
    for pos in map:
      n = occ_neighbors(map,*pos,see)
      if n == 0:
        map2[pos] =1
      elif n >= toleranz:
        map2[pos] =0
    occ2 = sum(map2.values())
    if occ1 == occ2: return occ2
    occ1 = occ2
    map = map2
    
puzzle = puzzle_einlesen('Tag_11.txt')

start = time.perf_counter()
print(löse(puzzle,1,4),  time.perf_counter()-start)

start = time.perf_counter()
print(löse(puzzle,100,5), time.perf_counter()-start)