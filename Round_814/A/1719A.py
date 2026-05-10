import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if (n+m)%2:
        print('Burenka')
    else:
        print('Tonya')