import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    b %= 2
    
    if b and a < 2:
        print('NO')
    elif a % 2 == 0:
        print('YES')
    else:
        print('NO')
    