import sys
input = sys.stdin.readline
from functools import reduce

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    ans = 0
    for b in range(30, -1, -1):
        need = 0
        for a in A:
            if (a>>b) & 1 == 0:
                need += 1
        
        if need <= k:
            k -= need
            ans |= (1<<b)
            
    print(ans)
