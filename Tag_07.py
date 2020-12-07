from collections import defaultdict, deque
import time

def puzzle_einlesen(datei):
  with open(datei) as f:
    return [rule for zeile in f for rule in zeile.strip().split(', ')]


def löse(puzzle):
  bag_is_contained_in = defaultdict(list)
  bag_contains = defaultdict(list)
  for rule in puzzle:
    words = rule.split()
    if len(words) > 5:
      if words[4] == 'no': continue
      anz = int(words[4])
      parent = words[0]+words[1]
      child =  words[5]+words[6]
    else:
      anz = int(words[0])
      child =  words[1]+words[2]
    bag_is_contained_in[child].append(parent)
    bag_contains[parent].append((child,anz))
  
  Q = deque(['shinygold'])
  bags_with_gold = set()
  while Q:
    child = Q.popleft()
    if child in bags_with_gold: continue
    bags_with_gold.add(child)
    for parent in bag_is_contained_in[child]:
      Q.append(parent)
  return len(bags_with_gold)-1, dfs(bag_contains, 'shinygold')-1    

def dfs(tree, node):
  counter = 1
  for child, anz in tree[node]:
    counter += anz * dfs(tree, child)
  return counter  





puzzle = puzzle_einlesen('Tag_07.txt')


start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)