import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    Sum = sum(A)
    if (math.isqrt(Sum)) ** 2 == Sum:
        print('YES')
    else:
        print('NO')