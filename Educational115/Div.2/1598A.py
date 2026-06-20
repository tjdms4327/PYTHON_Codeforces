import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(2)]
    
    queue = deque([(0,0)])
    visited = [[False]*n for _ in range(2)]
    visited[0][0] = True
    
    D = [(1,0), (1,1), (1, -1), (-1,1), (-1,0), (-1,-1), (0,1),(0,-1)]
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in D:
            nr, nc = r+dr, c+dc
            
            if 0<=nr<2 and 0<=nc<n:
                if matrix[nr][nc]==0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    
    if visited[1][n-1]:
        print('YES')
    else:
        print('NO')                    