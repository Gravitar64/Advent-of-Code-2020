import time
from collections import defaultdict


def read_puzzle(file):
  with open(file) as f:
    return f.read().splitlines()


def solve(puzzle):
  allergens, ingreds_food = {}, []
  for zeile in puzzle:
    a, b = zeile.rstrip(')').split('(contains ')
    ingreds = a.split()
    ingreds_food.append(ingreds)
    for alrg in b.split(', '):
      if alrg not in allergens:
        allergens[alrg] = set(ingreds)
      else:
        allergens[alrg] &= set(ingreds)
  ingreds_with_alrgs = set(i for ii in allergens.values() for i in ii)
  part1 = sum(
      1 for ii in ingreds_food for i in ii if i not in ingreds_with_alrgs)

  change = True
  while change:
    change = False
    ones = [(alrg, next(iter(ingrds)))
            for alrg, ingrds in allergens.items() if len(ingrds) == 1]
    for _, i1 in ones:
      for i2 in allergens.values():
        if len(i2) == 1 or i1 not in i2:
          continue
        i2.remove(i1)
        change = True

  part2 = ','.join([i for _, i in sorted(ones)])
  return part1, part2


puzzle = read_puzzle('Tag_21.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)
