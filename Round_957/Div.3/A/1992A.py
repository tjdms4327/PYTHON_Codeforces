import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    
    for _ in range(5):
        nums.sort()
        nums[0] += 1
        
    print(math.prod(nums))
    
    