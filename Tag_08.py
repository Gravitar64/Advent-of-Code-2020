import time

def puzzle_einlesen(datei):
  with open(datei) as f:
    return [[ins for ins in zeile.strip().split()] for zeile in f]

class Intcode:
  def __init__(self, puzzle):
    self.prog = [[opc, int(val)] for opc, val in puzzle]
    self.pc = 0
    self.acc = 0
    self.instructions = {'acc': self._acc, 'nop': self._nop, 'jmp': self._jmp}
    self.terminate = False

  def _acc(self, v):
    self.acc += v
    self.pc += 1

  def _jmp(self, v):
    self.pc += v

  def _nop(self, v):
    self.pc += 1

  def step(self):
    if self.pc >= len(self.prog):
      self.terminate = True
      return
    opc, val = self.prog[self.pc]
    self.instructions[opc](val)


def löse(puzzle):
  executed_instructions = set()
  intcode = Intcode(puzzle)
  while True:
    if intcode.pc in executed_instructions:
      return intcode.acc
    executed_instructions.add(intcode.pc)
    intcode.step()


def löse2(puzzle):
  nop2jmp = [i for i in range(len(puzzle)) if puzzle[i][0] in ('jmp', 'nop')]
  for change in nop2jmp:
    executed_instructions = set()
    puzzle[change][0] = 'jmp' if puzzle[change][0] == 'nop' else 'nop'
    intcode = Intcode(puzzle)
    while True:
      if intcode.pc in executed_instructions:
        break
      executed_instructions.add(intcode.pc)
      intcode.step()
      if intcode.terminate:
        return intcode.acc
    puzzle[change][0] = 'jmp' if puzzle[change][0] == 'nop' else 'nop'


puzzle = puzzle_einlesen('Tag_08.txt')

start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(löse2(puzzle), time.perf_counter()-start)
