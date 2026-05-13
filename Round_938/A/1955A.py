import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    
    res = min(
        n*a, (n//2)*b+(n%2)*a
    )
    print(res)