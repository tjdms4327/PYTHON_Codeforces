import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    a = n % 12
    if a!=10:
        b = n - a
        print(a, b)
    elif a == 10:
        a += 12
        b = n - a
        if b>=0:
            print(a, b)
        else:
            print(-1)
    
