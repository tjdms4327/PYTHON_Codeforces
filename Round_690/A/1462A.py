import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int, input().split()))
    
    res = []
    left, right = 0, n-1
    while left <= right:
        if left == right:
            res.append(B[left])
        else:
            res.append(B[left])
            res.append(B[right])
        left += 1
        right -= 1
        
    print(*res)