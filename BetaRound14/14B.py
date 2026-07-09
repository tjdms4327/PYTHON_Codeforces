import sys
input = sys.stdin.readline

n, x0 = map(int, input().split())


INF = float('inf')

L, R = -INF, INF
for _ in range(n):
    a, b = map(int, input().split())
    if a>b:
        a, b = b, a
    
    R = min(R, b)
    L = max(L, a)
    


if L > R:
    print(-1)
elif L <= x0 <= R:
    print(0)
elif x0 < L:
    print(L-x0)
elif x0 > R:
    print(x0 - R)