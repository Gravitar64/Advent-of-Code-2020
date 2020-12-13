import time

def read_puzzle(file):
  with open(file) as f:
    ts = f.readline()
    ids = [x for x in f.readline().split(',')]
    return int(ts), ids


def solve1(ts,ids):
  ids = [int(id) for id in ids if id != 'x']
  diff,id = sorted([(id - ts % id, id) for id in ids])[0]
  return diff * id


def solve2(ids):
  ids = [(start, int(id)) for start,id in enumerate(ids) if id != 'x']
  ts = 0
  lcm = 1
  for start, step in ids:
    while(ts + start) % step != 0:
      ts += lcm
    lcm *= step
  return ts    
  


ts, ids = read_puzzle('Tag_13.txt')

start = time.perf_counter()
print(solve1(ts,ids),  time.perf_counter()-start)

start = time.perf_counter()
print(solve2(ids),  time.perf_counter()-start)