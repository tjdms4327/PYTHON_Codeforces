import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(input().strip())
    
    cnt = Counter(a)
    
    ans = 0
    for x in 'ABCDEFG':
        v = cnt.get(x, 0)
        if v < m:
            ans += m-v
            
    print(ans)