import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(min(max(2*a, b), max(2*b, a), a+b)**2)