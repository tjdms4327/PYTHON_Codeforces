import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, w = map(int, input().split())

    count = (n//w) * (w-1)
    cur = (n//w) * w
    count += n - cur
    
    print(count)
