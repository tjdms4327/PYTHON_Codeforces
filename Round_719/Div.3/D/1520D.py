import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    cnt = defaultdict(int)
    ans = 0
    
    for i in range(n):
        v = A[i]-i
        ans += cnt[v]
        cnt[v] += 1
        
    print(ans)