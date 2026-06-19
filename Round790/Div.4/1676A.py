import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    nums = list(map(int, input().strip()))
    
    if sum(nums[:3]) == sum(nums[-3:]):
        print('YES')
    else:
        print('NO')