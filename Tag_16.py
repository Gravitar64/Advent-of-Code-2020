import time, re, math
from collections import defaultdict

def read_puzzle(file):
  valids = set()
  rule_dict = {}

  with open(file) as f:
    rules, mine, nearby = f.read().split('\n\n')
  
  for zeile in rules.splitlines():
    name, regeln = zeile.split(': ')
    l = [int(x) for x in re.findall('\d+', regeln)]
    v = set(range(l[0],l[1]+1)) | set(range(l[2],l[3]+1))
    valids.update(v)
    rule_dict[name] = v



  tickets = [[int(x) for x in re.findall('\d+', mine)]]
  tickets.extend([[int(x) for x in re.findall('\d+', t)] for t in nearby.split('\n')[1:]])
  return valids, tickets, rule_dict  


def solve(valids, tickets, rule_dict):
  par1 = sum([feld for t in tickets for feld in t if feld not in valids])

  for t in reversed(tickets):
    if all([feld in valids for feld in t]): continue
    tickets.remove(t)
  
  poss = defaultdict(list)
  for name, rule in rule_dict.items():
    for pos in range(len(tickets[0])):
      if not {t[pos] for t in tickets}.issubset(rule): continue
      poss[name].append(pos)

  while True:
    change = False
    ones = [pos[0] for pos in poss.values() if len(pos) == 1]
    for one in ones:
      for name, pos in poss.items():
        if len(pos) == 1: continue
        if one in pos:
          poss[name].remove(one)
          change = True
    if not change:
      break
  myTicket = tickets[0]
  part2 = math.prod([myTicket[i[0]] for n,i in poss.items() if 'departure' in n])
  return par1, part2 

puzzle = read_puzzle('Tag_16.txt')

start = time.perf_counter()
print(solve(*puzzle), time.perf_counter()-start)
