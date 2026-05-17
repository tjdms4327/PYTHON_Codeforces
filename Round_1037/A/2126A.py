import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x = list(map(int, input().strip()))
    print(min(x))