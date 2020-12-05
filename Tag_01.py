from itertools import combinations
import math

def puzzle_einlesen(datei):
  with open(datei) as f:
    return [int(x) for x in f]

def löse(puzzle,n):
  for c in combinations(puzzle,n):
    if sum(c) != 2020: continue
    return math.prod(c)    


puzzle = puzzle_einlesen('Tag_01.txt')
print(löse(puzzle,2))    
print(löse(puzzle,3))    
    