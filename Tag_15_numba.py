import numpy as np

from numba import njit
from time import perf_counter as pfc


nums = np.array([18,8,0,5,4,1,20], dtype=np.int32)

@njit("int32(int32[:], int32)")
def day15(nums, N):
    last = np.full(N, -1, dtype=np.int32)
    for i, x in enumerate(nums[:-1]):
        last[x] = i
    buffer = nums[-1]
    for i in range(len(nums) - 1, N - 1):
        y = 0 if last[buffer] == -1 else i - last[buffer]
        last[buffer], buffer = i, y
    return buffer

print(day15(nums, 2020))
start = pfc()
print(day15(nums, 30_000_000))
print(pfc()-start)