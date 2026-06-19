import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    diag1 = defaultdict(int)
    diag2 = defaultdict(int)
    for r in range(n):
        for c in range(m):
            diag1[r-c] += matrix[r][c]
            diag2[r+c] += matrix[r][c]
            
    best = 0
    for r in range(n):
        for c in range(m):
            cur = diag1[r-c] + diag2[r+c] - matrix[r][c]
            best = max(cur, best)
            
    print(best)    
    #print()