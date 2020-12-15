import time
import copy
from collections import defaultdict

def read_puzzle(file):
  p = defaultdict(list)
  with open(file) as f:
    for i,num in enumerate(f.readline().split(',')):
      p[int(num)].append(i+1)
  return p  
  

def solve(p,lastTurn):
  last = list(p.keys())[-1]
  turn = len(p)
  while turn < lastTurn:
    turn += 1
    if len(p[last]) > 1:
      akt = p[last][-1] - p[last][-2]
    else:
      akt = 0
    p[akt].append(turn)
    last = akt
  return akt      


puzzle = read_puzzle('Tag_15.txt')

start = time.perf_counter()
print(solve(copy.deepcopy(puzzle),2020),  time.perf_counter()-start)

start = time.perf_counter()
print(solve(puzzle,30_000_000),  time.perf_counter()-start)

