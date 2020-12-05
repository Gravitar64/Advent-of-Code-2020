import time


def puzzle_einlesen(datei):
  puzzle=[]
  with open(datei) as f:
    return [x.strip() for x in f]


def löse(puzzle):
  maxID, minID = 0, 999999
  gebuchte_sids = set()
  for bp in puzzle:
    rl,rh = 0,127
    cl,ch = 0,7
    for c in bp:
      if c == 'F': rh -= (rh-rl)//2+1
      if c == 'B': rl += (rh-rl)//2+1
      if c == 'R': cl += (ch-cl)//2+1
      if c == 'L': ch -= (ch-cl)//2+1
    sid = min(rl,rh)*8+max(cl,ch)
    gebuchte_sids.add(sid)
    maxID = max(sid, maxID)
    minID = min(sid, minID)
  denkbare_sids = {sid for sid in range(1024) if minID < sid < maxID}
  return maxID, denkbare_sids-gebuchte_sids
  

puzzle = puzzle_einlesen('Tag_05.txt')
start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)