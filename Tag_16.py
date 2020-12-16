from os import truncate
import time
from collections import defaultdict

def read_puzzle(file):
  rules, myTicket, tickets = defaultdict(set), [], []
  with open(file) as f:
    part = 0
    for z in [x.strip() for x in f]:
      if not z:
        part += 1
        continue
      if part == 0:
        ruleName,p2 = z.split(': ')
        p1,p2 = p2.split(' or ')
        p3,p4 = p1.split('-')
        p5,p6 = p2.split('-')
        rules[ruleName].update(range(int(p3),int(p4)+1))
        rules[ruleName].update(range(int(p5),int(p6)+1))
      elif part == 1:
        myTicket = [int(x) for x in z.split(',')]
      else:
        tickets.append([int(x) for x in z.split(',')])
  return rules, myTicket, tickets      


    

def solve(rules,tickets):
  all_rules = {x for s in rules.values() for x in s}
  return sum([field for t in tickets for field in t if field not in all_rules])


def solve2(rules,myTicket,tickets):
  positions = defaultdict(list)
  all_rules = {x for s in rules.values() for x in s}
  delTickets = [i for i,t in enumerate(tickets) for field in t if field not in all_rules]
  for i in reversed(delTickets):
    del tickets[i]
  tickets.append(myTicket)
  for name,rule in rules.items():
    for pos in range(len(tickets[0])):
      if all([t[pos] in rule for t in tickets]):
        positions[name].append(pos)
  while True:
    change = False
    for name,poss in positions.items():
      if len(poss) == 1:
        for n1,p2 in positions.items():
          if len(p2) == 1: continue
          if poss[0] in p2:
            positions[n1].remove(poss[0])
            change = True
    if not change:
      break
  product = 1
  for name,idx in positions.items():
    if 'departure' not in name: continue
    product *= myTicket[idx[0]]
  return product  





           
  

rules, myTicket, tickets = read_puzzle('Tag_16.txt')

start = time.perf_counter()
print(solve(rules, tickets),time.perf_counter()-start)

start = time.perf_counter()
print(solve2(rules,myTicket,tickets),time.perf_counter()-start)