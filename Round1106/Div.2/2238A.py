import sys
input = sys.stdin.readline

INF = float('inf')

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    tot = INF
    if all(a>=b for a, b in zip(A, B)):
        tot = sum(a-b for a, b in zip(A, B))
        
    A.sort()
    B.sort()
    if all(a>=b for a, b in zip(A, B)):
        tot = min(tot, c+sum(a-b for a, b in zip(A, B)))
        
    
    
    if tot == INF:
        print(-1)
    else:
        print(tot)