import time
from collections import Counter
import itertools as iter


def read_puzzle(file):
  with open(file) as f:
    return [x.strip() for x in f]


def neighbors(pos):
   for delta in iter.product(range(-1, 2), repeat=len(pos)):
    if delta ==  (0,) * len(pos): continue
    yield tuple([a+b for a,b in zip(pos, delta)])


def solve(puzzle, dim):
  active = {tuple([x, y]+[0]*(dim-2)) for y, z in enumerate(puzzle)
           for x, c in enumerate(z) if c == '#'}
  for _ in range(6):
    neighb = Counter([p for pos in active for p in neighbors(pos)])
    active = {pos for pos, anz in neighb.items() if anz == 3 or (anz == 2 and pos in active)}
  return len(active)


puzzle = read_puzzle('Tag_17.txt')

for dim in range(3,5):
  start = time.perf_counter()
  print(solve(puzzle, dim), time.perf_counter()-start)