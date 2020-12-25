import time
from collections import Counter


def read_puzzle(file):
  with open(file) as f:
    return [line.strip() for line in f]


def get_neighors(x,y):
  for dx, dy in dirs.values():
    yield x+dx, y+dy


def solve(puzzle):
  endPos = []
  for line in puzzle:
    pos = 0
    x = y = 0
    while pos < len(line):
      for l in range(1, 3):
        if (char := line[pos:pos+l]) in dirs:
          dx, dy = dirs[char]
          x += dx
          y += dy
          pos += l
          break
    endPos.append((x, y))
  
  blacks = {pos for pos, anz in Counter(endPos).items() if anz % 2 == 1}
  part1 = len(blacks)

  for _ in range(100):
    neighb = Counter([p for pos in blacks for p in get_neighors(*pos)])
    blacks = {pos for pos, anz in neighb.items() 
    if anz == 2 or (anz == 1 and pos in blacks)}

  return part1, len(blacks)


puzzle = read_puzzle('Tag_24.txt')

dirs = dict(e=(2, 0), se=(1, 1), sw=(-1, 1),
            w=(-2, 0), nw=(-1, -1), ne=(1, -1))

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)