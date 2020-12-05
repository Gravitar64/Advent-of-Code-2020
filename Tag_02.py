import time

def puzzle_einlesen(datei):
  puzzle = []
  with open(datei) as f:
    for zeile in f:
      anz, buchst, passw = zeile.split()
      mi, ma = [int(x) for x in anz.split('-')]
      buchst = buchst[0]
      puzzle.append((mi,ma,buchst,passw))
  return puzzle    

def löse(puzzle):
  counter = 0
  for mi, ma, buchst, passw in puzzle:
    if mi <= passw.count(buchst) <= ma: counter += 1
  return counter   

def löse2(puzzle):
  counter = 0
  for mi, ma, buchst, passw in puzzle:
    if (passw[mi-1]+passw[ma-1]).count(buchst) == 1: counter += 1
  return counter   


puzzle = puzzle_einlesen('Tag_02.txt')

start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(löse2(puzzle), time.perf_counter()-start)    
    