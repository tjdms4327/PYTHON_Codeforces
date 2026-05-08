import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    cnt, rest = n//2020, n%2020
    if cnt >= rest:
        print('YES')
    else:
        print('NO')