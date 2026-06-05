import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w, h, n = map(int, input().split())
    
    cnt = 1
    while w%2==0:
        cnt *= 2
        w //= 2
    while h%2==0:
        cnt *= 2
        h //= 2
        
    if cnt >= n:
        print('YES')
    else:
        print('NO')