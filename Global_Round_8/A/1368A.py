import sys
input = sys.stdin.readline
from math import ceil


t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    
    cnt = 0
    while max(a, b) <= n:
        if a < b:
            a += b
        else:
            b += a
            
        cnt += 1
    
    print(cnt)