import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    
    d = abs(a-b)-1
    if d%2:
        print('YES')
    else:
        print('NO')