import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    grid = [list(input().strip()) for _ in range(3)]
    
    for row in grid:
        if '?' in row:
            row.remove('?')
            print(*({'A','B','C'}-set(row)))
            break