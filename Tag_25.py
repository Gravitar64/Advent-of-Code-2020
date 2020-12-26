import time


def read_puzzle(file):
  with open(file) as f:
    return [int(line.strip()) for line in f]


def find_loop(pub, value, loop):
  while value != pub:
    value, loop = (value * 7) % DIVIDER, loop + 1
  return loop


def solve(puzzle):
  return pow(puzzle[1], find_loop(puzzle[0], 1, 0), DIVIDER)


puzzle = read_puzzle('Tag_25.txt')
DIVIDER = 20201227

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)
