import time
import re


def read_puzzle(file):
  with open(file) as f:
    return f.read().split('\n\n')


def dfs(tree, node, depth):
  if depth > 20: return ''
  searchstr = '('
  for next in tree[node].split():
    if next == '|':
      searchstr += next
    elif next.isdigit():
      searchstr += dfs(tree, next, depth+1)
    else:
      return next[1]  
  return searchstr+')'


def solve(rules, messages, part1=True):
  if not part1:
    rules += '\n8: 42 | 42 8\n11: 42 31 | 42 11 31'
  rules = dict([zeile.split(': ') for zeile in rules.split('\n')])
  r = re.compile(dfs(rules, '0', 0))
  return sum([1 for m in messages.split() if r.fullmatch(m)])


puzzle = read_puzzle('Tag_19.txt')

start = time.perf_counter()
print(solve(*puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(solve(*puzzle, False), time.perf_counter()-start)
