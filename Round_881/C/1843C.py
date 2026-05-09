import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    res = 0
    while n > 0:
        res += n
        n //= 2
    print(res)