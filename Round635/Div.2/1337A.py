import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
        
    x, y, z = b, c, c
    print(x, y, z)