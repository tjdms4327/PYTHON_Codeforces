import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())

    count = sum(1 for x in [b, c, d] if x > a)
    print(count)
