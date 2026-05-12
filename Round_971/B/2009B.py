import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [list(input().strip()) for _ in range(n)]
    
    res = []
    for row in matrix[::-1]:
        res.append(row.index('#')+1)
        
    print(*res)