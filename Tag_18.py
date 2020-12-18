import time


def read_puzzle(file):
  with open(file) as f:
    return [x.strip().replace(' ','') for x in f]

def rechne(zahl1, zahl2, op):
  return zahl1 + zahl2 if op == '+' else zahl1 * zahl2

def priorität(op, part1):
  if part1:
    return 1 if op in '+*' else 0
  else:
    if op == '+': return 2
    if op == '*': return 1
    return 0    

def solve(puzzle, part1=True):
  summe = 0
  for zeile in puzzle:
    zahlen, ops = [], []
    for ch in zeile:
      if ch.isdigit():
        zahlen.append(int(ch))
      elif ch == '(':
        ops.append(ch)
      elif ch == ')':
        while ops[-1] != '(':
          zahlen.append(rechne(zahlen.pop(), zahlen.pop(), ops.pop()))
        ops.pop()
      elif ch in '+*':
        while ops and priorität(ops[-1], part1) >= priorität(ch, part1):
          zahlen.append(rechne(zahlen.pop(), zahlen.pop(), ops.pop()))
        ops.append(ch)
    while ops:
      zahlen.append(rechne(zahlen.pop(), zahlen.pop(), ops.pop()))
    summe += zahlen[0]
  return summe          

puzzle = read_puzzle('Tag_18.txt')

start = time.perf_counter()
print(solve(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(solve(puzzle, False), time.perf_counter()-start)
