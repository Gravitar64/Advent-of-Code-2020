import time

def puzzle_einlesen(datei):
  with open(datei) as f:
    ts = f.readline()
    ids = [x for x in f.readline().split(',')]
    return int(ts), ids


def löse(ts,ids):
  ids = [int(id) for id in ids if id != 'x']
  diff,id = sorted([(id - ts % id, id) for id in ids])[0]
  return diff * id


def löse2(ids):
  ids = [(start,int(id)) for start, id in enumerate(ids) if id != 'x']
  position = 0
  kgV = 1
  for start, step in ids:
    #print(f'Bus {step} startet bei TS {start}')
    while (position + start) % step != 0:
      position += kgV
    kgV *= step
    #print(f'Position: {position}, kgV: {kgV}')
  return position  


ts, ids = puzzle_einlesen('Tag_13.txt')

start = time.perf_counter()
print(löse(ts,ids),  time.perf_counter()-start)

start = time.perf_counter()
print(löse2(ids),  time.perf_counter()-start)