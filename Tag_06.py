import time
from collections import Counter


def puzzle_einlesen(datei):
  with open(datei) as f:
    return [x for x in f.read().split('\n\n')]


def löse(puzzle):
  return sum([len({c for c in group.replace('\n', '')}) for group in puzzle])


def löse2(puzzle):
  summe = 0
  for group in puzzle:
    gruppengröße = group.count('\n')+1
    antworten = Counter(group)
    summe += sum([1 for anz in antworten.values() if anz == gruppengröße])
  return summe


puzzle = puzzle_einlesen('Tag_06.txt')

start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(löse2(puzzle), time.perf_counter()-start)
