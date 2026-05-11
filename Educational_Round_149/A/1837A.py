import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    
    if x%k:
        print(1)
        print(x)
    else:
        print(2)
        print(x+1, -1)