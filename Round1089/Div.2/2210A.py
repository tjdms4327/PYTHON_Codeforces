import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    ans = list(range(n, 0, -1))
    print(*ans)