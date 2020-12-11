import time


def puzzle_einlesen(datei):
  with open(datei) as f:
    p1 = sorted([int(zeile) for zeile in f])
    return [0]+p1+[p1[-1]+3]


def löse(puzzle):
  diffs = ''.join([str(b-a) for a, b in zip(puzzle, puzzle[1:])])
  part1 = diffs.count('1')*diffs.count('3')
  diffs = diffs.replace('1111', 'a').replace('111', 'b').replace('11', 'c')
  return part1, 7**diffs.count('a') * 4**diffs.count('b') * 2**diffs.count('c')

def löse_dp(puzzle):
  diffs = [b-a for a, b in zip(puzzle, puzzle[1:])]
  part1 = diffs.count(1)*diffs.count(3)
  möglichkeiten = [1]+[0]*puzzle[-1]
  for jolt in puzzle[1:]:
    möglichkeiten[jolt] = möglichkeiten[jolt-3]+möglichkeiten[jolt-2]+möglichkeiten[jolt-1]
  return part1, möglichkeiten[-1]     



puzzle = puzzle_einlesen('Tag_10.txt')

start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(löse_dp(puzzle), time.perf_counter()-start)