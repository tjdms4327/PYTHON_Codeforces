import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    X = list(map(int, input().split()))

    ans = b
    for x in X:
        ans += min(x, a-1)

    print(ans)