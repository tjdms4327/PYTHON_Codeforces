import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    ans = 0
    cost = 1
    while cost <= n:
        take = min(k, n // cost)
        ans += take
        n -= take * cost
        cost *= 2
    print(ans)
