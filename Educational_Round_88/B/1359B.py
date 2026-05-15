import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    matrix = [list(input().strip().split('*')) for _ in range(n)]
    
    tot = 0
    for row in matrix:
        for slice in row:
            length = len(slice)
            if length>=2 and y<2*x:
                tot += length//2*y
                tot += x if length%2 else 0
            else:
                tot += x * length
    
    print(tot)