import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    matrix = [list(input().strip()) for _ in range(8)]
    
    for col in zip(*matrix):
        col = ''.join(col)
        if col != '.'*8:
            res = ''.join(col)
            res = res.replace('.','')
            break
    
    print(res)