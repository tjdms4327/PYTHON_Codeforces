import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    cnt = Counter(A)
    
    INF = float('inf')
    ans = INF
    
    standard = max(cnt, key=cnt.get)
    for standard in set(A):
        left, right = 0,0
        for key, val in cnt.items():
            if key < standard:
                left += val
            elif key > standard:
                right += val
        
        temp = min(left, right)
        ans = min(ans, temp + (left-temp) + (right-temp))
            
    print(ans)