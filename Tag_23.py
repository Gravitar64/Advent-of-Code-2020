import time


def read_puzzle(file):
  with open(file) as f:
    return [int(x) for zeile in f for x in zeile]


def get_three(cups, current):
  three_cups = [cups[current]]
  for _ in range(2):
    three_cups.append(cups[three_cups[-1]])
  return three_cups


def solve(puzzle, moves):
  maxC, minC = max(puzzle), min(puzzle)
  current = puzzle[0]
  cups = {a: b for a, b in zip(puzzle, puzzle[1:])}
  cups[puzzle[-1]] = puzzle[0]

  for _ in range(moves):
    three_cups = get_three(cups, current)
    label = current-1
    while label < minC or label in three_cups:
      label -= 1
      if label < minC:
        label = maxC
    cups[current] = cups[three_cups[-1]]
    cups[three_cups[-1]] = cups[label]
    cups[label] = three_cups[0]
    current = cups[current]
  
  if moves == 100:
    part1 = str(cups[1])
    while part1[-1] != '1':
      part1 += str(cups[int(part1[-1])])
    return part1[:-1]
  else:
    return cups[1] * cups[cups[1]]


puzzle = read_puzzle('Tag_23.txt')

start = time.perf_counter()
print(solve(puzzle, 100), time.perf_counter()-start)

start = time.perf_counter()
print(solve(puzzle + list(range(10,1_000_001)), 10_000_000), time.perf_counter()-start)
