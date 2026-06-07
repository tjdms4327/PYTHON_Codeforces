import sys, math
input = sys.stdin.readline

def prime(num):
    if num < 2:
        return False
    for x in range(2, math.isqrt(num)+1):
        if num%x == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    
    if k == 1:
        if prime(x):
            print('YES')
        else:
            print('NO')
    else:
        if x == 1 and k == 2:
            print('YES')
        else:
            print('NO')