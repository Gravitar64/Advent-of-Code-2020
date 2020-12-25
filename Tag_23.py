import time
from collections import deque

def read_puzzle(file):
  with open(file) as f:
    return deque([int(x) for zeile in f for x in zeile])


def solve(cups,part2=False):
  if part2:
    cups.extend(range(max(cups)+1,10_001))
    moves = 100_000
  else:
    moves = 100 
  

  maxC, minC = max(cups), min(cups)
  for i in range(moves):
    curr_cup = cups[0]
    cups.rotate(-1)
    three_cups = [cups.popleft(), cups.popleft(), cups.popleft()]
    label = curr_cup-1
    while True:
      if label < minC:
        label = maxC
      if label in cups:
        dest_cup = cups.index(label)
        break
      label -= 1
    cups.rotate(-dest_cup-1)
    cups.extendleft(reversed(three_cups))
    cups.rotate(dest_cup+1)
  cups.rotate(-cups.index(1))
  if not part2:
    return ''.join(str(c) for c in cups)
  else:
    return [c for c in cups][:10] 




puzzle = read_puzzle('Tag_23.txt')

start = time.perf_counter()
print(solve(puzzle.copy()), time.perf_counter()-start)

start = time.perf_counter()
print(solve(puzzle, True), time.perf_counter()-start)