import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    a = [list(input().strip()) for _ in range(8)]
    
    for r in range(1, 7):
        for c in range(1, 7):
            if (
                a[r][c] == '#'
                and a[r-1][c-1] == '#'
                and a[r-1][c+1] == '#'
                and a[r+1][c-1] == '#'
                and a[r+1][c+1] == '#'
            ):
                print(r + 1, c + 1)
    