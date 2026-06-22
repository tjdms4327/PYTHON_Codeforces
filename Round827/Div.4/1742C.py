import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input() # 빈줄
    matrix = [input().strip() for _ in range(8)]
    
    if 'R'*8 in matrix:
        color = 'R'
    else:
        color = 'B'
    print(color)