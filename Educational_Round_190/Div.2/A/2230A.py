import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    
    alone = n * a
    group = (n//3)*b
    if n%3:
        temp = min(
            b, (n%3)*a
        )
        group += temp
    
    print(min(alone, group))
