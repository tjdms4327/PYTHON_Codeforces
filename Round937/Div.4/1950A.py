import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    
    if nums[0]<nums[1]<nums[2]:
        print('STAIR')
    elif nums[0]<nums[1] and nums[1]>nums[2]:
        print('PEAK')
    else:
        print('NONE')