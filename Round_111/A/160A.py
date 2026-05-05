import sys
input = sys.stdin.readline

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

twin = sum(coins)
cur = 0
for i in range(n-1, -1, -1):
    cur += coins[i]
    twin -= coins[i]
    if twin < cur:
        print(n - i)
        break
    