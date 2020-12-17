import time
from collections import Counter
import itertools as iter


class Vec(tuple):
  def __new__(cls, *args):
    return tuple.__new__(cls, args)

  def __add__(self, other):
    return Vec(*tuple(a+b for a, b in zip(self, other)))


def puzzle_einlesen(datei):
  with open(datei) as f:
    return [x.strip() for x in f]


def nachbarn(pos):
  for delta in iter.product(range(-1, 2), repeat=len(pos)):
    if all([n == 0 for n in delta]):
      continue
    yield pos + Vec(*delta)


def löse(puzzle, dim):
  karte = {Vec(*(x, y)+(0,)*(dim-2)) for y, z in enumerate(puzzle)
           for x, c in enumerate(z) if c == '#'}
  for _ in range(6):
    nachb = Counter([p for pos in karte for p in nachbarn(pos)])
    karte = {pos for pos, anz in nachb.items() if anz ==
             3 or (anz == 2 and pos in karte)}
  return len(karte)


puzzle = puzzle_einlesen('Tag_17.txt')

start = time.perf_counter()
print(löse(puzzle, 3), time.perf_counter()-start)

start = time.perf_counter()
print(löse(puzzle, 4), time.perf_counter()-start)
