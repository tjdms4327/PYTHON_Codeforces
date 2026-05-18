import sys
input = sys.stdin.readline
import math

t = int(input())
for _ in range(t):
    l, r= map(int, input().split())
    
    x = l
    y = 2*l # lcm = y
    
    if y <= r:
        print(x, y)
    else:
        print(-1, -1)  