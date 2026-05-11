import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    
    floor = 1
    if n > 2:
        n -= 2
        floor += n//x
        if n % x:
            floor += 1
            
    print(floor)