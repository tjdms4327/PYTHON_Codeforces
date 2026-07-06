import sys
input = sys.stdin.readline

n, m, boss = input().split()
n = int(n) ; m = int(m)
matrix = [input().strip() for _ in range(n)]

D = [(1,0), (-1,0), (0,1), (0,-1)]

staff = set()
for r in range(n):
    for c in range(m):
        if matrix[r][c] == boss:
            for dr, dc in D:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    if matrix[nr][nc] != '.' and matrix[nr][nc] != boss:
                        staff.add(matrix[nr][nc])

print(len(staff))