import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    possible = [False]*(n+1)
    for l in range(n):
        cur = A[l]
        for r in range(l+1, n):
            cur += A[r]
            if cur > n: # ai<=n이니까
                break
            possible[cur] = True
    
    cnt = Counter(A)
    ans = 0
    for x in range(1, n+1):
        if possible[x]:
            ans += cnt[x]
            
    print(ans)
