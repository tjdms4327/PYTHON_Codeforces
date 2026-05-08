import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    while n % 2 == 0:
        n //= 2
    
    if n != 1:
        print('YES')
    else:
        print('NO')