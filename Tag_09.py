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
  for i in range(len(puzzle)):
    summe = j = 0
    zahlen = set()
    while summe < invalid:
      summe += puzzle[i+j]
      zahlen.add(puzzle[i+j])
      if summe == invalid:
        return min(zahlen)+max(zahlen)
      j += 1  


puzzle = puzzle_einlesen('Tag_09.txt')

start = time.perf_counter()
invalid_number = löse(puzzle,25)
print(invalid_number, time.perf_counter()-start)

start = time.perf_counter()
print(löse2(puzzle,invalid_number), time.perf_counter()-start)
