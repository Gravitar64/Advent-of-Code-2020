import time


def read_puzzle(file):
  with open(file) as f:
    return [x.strip().split() for x in f]


def modifyBit(value, p, b):
  return (value & ~(1 << p)) | ((b << p) & (1 << p))


def possibleAdresses(addr, mask):
  for pos, char in enumerate(reversed(mask)):
    if char != '1':
      continue
    addr = modifyBit(addr, pos, 1)
  addresses = {addr}
  for pos, char in enumerate(reversed(mask)):
    if char != 'X':
      continue
    tmp_addr = set()
    for addr in addresses:
      for bit in range(2):
        tmp_addr.add(modifyBit(addr, pos, bit))
    addresses.update(tmp_addr)
  return addresses


def solve(p):
  mem1, mem2 = {}, {}
  for w1, _, w2 in p:
    if w1 == 'mask':
      mask = w2
    else:
      addr, value = int(w1[4:-1]), int(w2)
      v1 = value
      for pos, char in enumerate(reversed(mask)):
        if char == 'X':
          continue
        v1 = modifyBit(v1, pos, int(char))
      mem1[addr] = v1
      for addr in possibleAdresses(addr, mask):
        mem2[addr] = value
  return sum(mem1.values()), sum(mem2.values())


puzzle = read_puzzle('Tag_14.txt')

start = time.perf_counter()
print(solve(puzzle),  time.perf_counter()-start)