import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]

r1, r2 = -1, -1
for i in range(n):
    if '*' in matrix[i]:
        r2 = i
        if r1 == -1:
            r1 = i
            
c1, c2 = -1, -1
for i, col in enumerate(zip(*matrix)):
    if '*' in col:
        c2 = i
        if c1 == -1:
            c1 = i
            


for row in matrix[r1:r2+1]:
    print(''.join(row[c1:c2+1]))