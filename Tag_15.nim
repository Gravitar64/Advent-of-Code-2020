import algorithm, times

let nums = [18,8,0,5,4,1,20]

proc solve(nums:array,size:int): int =
    var buffer,y: int   
    var last: array[size, int]
    last.fill(-1)
    for i,x in nums[0..^2]:
        last[x] = i
    buffer = nums[^1]
    for i in len(nums)-1..size-2:
        y = if last[buffer] == -1: 0 else: i-last[buffer]
        last[buffer] = i
        buffer = y
    return buffer    

var start = getTime()
echo solve(nums,2020), ", Time taken: ", getTime() - start
start = getTime()
echo solve(nums,30_000_000), ", Time taken: ", getTime() - start
