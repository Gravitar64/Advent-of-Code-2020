import time
from collections import Counter
import itertools as iter


def puzzle_einlesen(datei):
  with open(datei) as f:
    return [x.strip() for x in f]


def nachbarn(pos):
   for delta in iter.product(range(-1, 2), repeat=len(pos)):
    if delta ==  (0,) * len(pos): continue
    yield tuple([a+b for a,b in zip(pos, delta)])


def löse(puzzle, dim):
  karte = {tuple([x, y]+[0]*(dim-2)) for y, z in enumerate(puzzle)
           for x, c in enumerate(z) if c == '#'}
  for _ in range(6):
    nachb = Counter([p for pos in karte for p in nachbarn(pos)])
    karte = {pos for pos, anz in nachb.items() if anz ==
             3 or (anz == 2 and pos in karte)}
  return len(karte)


puzzle = puzzle_einlesen('Tag_17.txt')

for dim in range(3,4):
  start = time.perf_counter()
  print(löse(puzzle, dim), time.perf_counter()-start)