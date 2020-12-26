import time


def read_puzzle(file):
  with open(file) as f:
    return [int(line.strip()) for line in f]


def find_loop(pub_key, value, loop):
  while value != pub_key:
    loop += 1
    value = (value * 7) % 20201227
  return loop


def gen_secret(pub_key, loop, value):
  for _ in range(loop):
    value = (value * pub_key) % 20201227
  return value


def solve(puzzle):
  l = find_loop(puzzle[0],1,0)
  return gen_secret(puzzle[1],l,1)


puzzle = read_puzzle('Tag_25.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)
