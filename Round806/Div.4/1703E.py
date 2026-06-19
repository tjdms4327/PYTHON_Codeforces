import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = [list(input().strip()) for _ in range(n)]
    
    ans = 0
    
    for i in range(n//2):
        for j in range((n+1)//2):
            vals = [
                a[i][j],
                a[j][n-1-i],
                a[n-1-i][n-1-j],
                a[n-1-j][i]
            ]
            
            cnt = Counter(vals)
            ans += min(cnt['0'], cnt['1'])
    
    print(ans)