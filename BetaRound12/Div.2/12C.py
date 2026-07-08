import sys
input = sys.stdin.readline
from collections import Counter

n, m = map(int, input().split())

prices = list(map(int, input().split()))
prices.sort()
reversed_prices = prices[::-1]

names = [input().strip() for _ in range(m)]
cnt = sorted(Counter(names).values(), reverse=True)

min_tot, max_tot = 0,0
i = 0
for val in cnt:
    min_tot += val*prices[i]
    max_tot += val*reversed_prices[i]
    i += 1
    
print(min_tot, max_tot)