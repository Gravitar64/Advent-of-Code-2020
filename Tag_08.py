import time

def puzzle_einlesen(datei):
  with open(datei) as f:
    return [zeile.strip().split() for zeile in f]

class Opcode:
  def __init__(self, puzzle):
    self.prog = puzzle.copy()
    self.pc = 0
    self.acc = 0

  def step(self):
    if self.pc >= len(self.prog): return self.acc
    opc, val = self.prog[self.pc]
    if opc == 'acc': self.acc += int(val)
    if opc == 'jmp': self.pc += int(val)
    if opc != 'jmp': self.pc += 1

def löse(puzzle):
  opcode = Opcode(puzzle)
  executed = set()
  while True:
    if opcode.pc in executed: return opcode.acc
    executed.add(opcode.pc)
    opcode.step()





def löse2(puzzle):
  nop2jmp = [i for i,instr in enumerate(puzzle) if instr[0] in ('jmp', 'nop')]
  for i in nop2jmp:
    puzzle[i][0] = 'jmp' if puzzle[i][0] == 'nop' else 'nop'
    executed = set()
    opcode = Opcode(puzzle)
    while True:
      if opcode.pc in executed: break
      executed.add(opcode.pc)
      e = opcode.step()
      if e: return e
    puzzle[i][0] = 'jmp' if puzzle[i][0] == 'nop' else 'nop'





puzzle = puzzle_einlesen('Tag_08.txt')


start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(löse2(puzzle), time.perf_counter()-start)
