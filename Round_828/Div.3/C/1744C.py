import sys
input = sys.stdin.readline
from bisect import bisect_left
bl = bisect_left

t = int(input())
for _ in range(t):
    n, c = input().strip().split() ; n = int(n)
    s = list(input().strip())
    
    if c == 'g':
        print(0)
        continue
    
    
    ss = s + s
    green = []
    for i, ch in enumerate(ss):
        if ch == 'g':
            green.append(i)
            
    ans = 0
    for i in range(n):
        if s[i] == c:
            j = green[bl(green, i)] # i 뒤의 첫 green 위치
            ans = max(ans, j-i)
            
    print(ans)
            