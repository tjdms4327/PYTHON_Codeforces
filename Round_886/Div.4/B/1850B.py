import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    res = []
    for i in range(1, n+1):
        a, b = map(int, input().split())
        if a <= 10:
            res.append((b, i))
    res.sort(reverse=True)
    
    print(res[0][1])