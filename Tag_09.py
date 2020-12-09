import time


def puzzle_einlesen(datei):
  with open(datei) as f:
    return [int(zeile) for zeile in f]


def löse(puzzle, preamble):
  for i in range(len(puzzle)):
    pre_numbers = set(puzzle[i:i+preamble])
    check_number = puzzle[i+preamble]
    for n in pre_numbers:
      if check_number-n in pre_numbers: break
    else:
      return(check_number)

def löse2(puzzle,invalid):
  low, high = 0,1
  while True:
    summe = sum(puzzle[low:high])
    if summe < invalid:   
      high +=1
    elif summe > invalid: 
      low += 1
    else: 
      return max(puzzle[low:high])+min(puzzle[low:high])


puzzle = puzzle_einlesen('Tag_09.txt')

start = time.perf_counter()
invalid_number = löse(puzzle,25)
print(invalid_number, time.perf_counter()-start)

start = time.perf_counter()
print(löse2(puzzle,invalid_number), time.perf_counter()-start)
