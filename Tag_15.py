import time
from collections import defaultdict
import copy

def read_puzzle(file):
  p = defaultdict(list)
  with open(file) as f:
    for i,num in enumerate(f.readline().split(',')):
      p[int(num)].append(i+1)
  return p
  

def solve(p,last_round):
  last_num = list(p.keys())[-1]
  runde = len(p)
  while runde < last_round:
    runde +=1
    if len(p[last_num]) > 1:
      akt = p[last_num][-1] - p[last_num][-2]
    else:
      akt = 0
    p[akt].append(runde)
    last_num = akt
  return akt      


puzzle = read_puzzle('Tag_15.txt')

start = time.perf_counter()
print(solve(copy.deepcopy(puzzle),2020),time.perf_counter()-start)

start = time.perf_counter()
print(solve(puzzle,30_000_000),time.perf_counter()-start)

