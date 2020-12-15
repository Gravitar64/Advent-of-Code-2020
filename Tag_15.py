import time

def read_puzzle(file):
  with open(file) as f:
    return [int(x) for x in f.readline().split(',')]
    

def solve(p,last_round):
  nums = {num:i for i,num in enumerate(p[:-1],1)}
  last_num = p[-1]
  for pos in range(len(p),last_round):
    last_pos = nums.get(last_num, pos)
    nums[last_num] = pos
    last_num = pos - last_pos
  return last_num      

puzzle = read_puzzle('Tag_15.txt')

start = time.perf_counter()
print(solve(puzzle,2020),time.perf_counter()-start)

start = time.perf_counter()
print(solve(puzzle,30_000_000),time.perf_counter()-start)