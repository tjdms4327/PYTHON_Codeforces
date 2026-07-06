import sys
input = sys.stdin.readline

matrix = [list(input().strip()) for _ in range(8)]

black = 0
for row in matrix:
    if set(row) == set(['B']):
        black += 1
        
if black < 8:
    for col in zip(*matrix):
        if set(col) == set(['B']):
            black += 1
            
print(black)