import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    x1, x2, x3 = map(int, input().split())

    best = 31
    for a in range(1, 11, 1):
        tot = abs(x1-a) + abs(x2-a) + abs(x3-a)
        best = min(best, tot)
        
        
    print(best)