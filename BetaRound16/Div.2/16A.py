import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]

for i in range(n):
    if len(set(matrix[i])) > 1:
        print('NO')
        break
    
    if i == 0:
        continue
    if matrix[i][0] == matrix[i-1][0]:
        print('NO')
        break
    
else:
    print('YES')