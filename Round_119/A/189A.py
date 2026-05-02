import sys
input = sys.stdin.readline

n, a, b, c = map(int, input().split())

dp = [-10**9]*(n+1)
dp[0] = 0
for i in range(1, n + 1):
    if i - a >= 0:
        dp[i] = max(dp[i], dp[i - a] + 1)
    if i - b >= 0:
        dp[i] = max(dp[i], dp[i - b] + 1)
    if i - c >= 0:
        dp[i] = max(dp[i], dp[i - c] + 1)
        
print(dp[n])
