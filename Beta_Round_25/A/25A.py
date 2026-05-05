import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

even = sum(1 for x in nums if x%2==0)

for i in range(n):
    if even==1:
        if nums[i]%2==0:
            res = i+1
            break
    else:
        if nums[i]%2==1:
            res = i+1
            break

print(res)