import time

def puzzle_einlesen(datei):
  with open(datei) as f:
    return [int(''.join(['0' if c in 'FL' else '1' for c in zeile.strip()]),2) for zeile in f]
  
def löse(puzzle):
  puzzle.sort()
  for sid1,sid2 in zip(puzzle,puzzle[1:]):
    if sid2-sid1 != 1:
      sid = sid2-1
      break
  return puzzle[-1], sid 
  
puzzle = puzzle_einlesen('Tag_05.txt')
start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)