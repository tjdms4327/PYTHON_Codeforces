import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

MAXV = max(A)
dp = [0] * (MAXV+1)
dp[1] = cnt[1]
for i in range(2, MAXV+1):
    dp[i] = max(dp[i-1], dp[i-2] + cnt[i]*i)

print(max(dp))
