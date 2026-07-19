import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    
    while n and x//2+10<x:
        n -= 1
        x = x//2 + 10
        
    x -= 10*m
    
    if x<=0:
        print('YES')
    else:
        print('NO')