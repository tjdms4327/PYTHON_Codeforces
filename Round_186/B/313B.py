import sys
input = sys.stdin.readline

s = list(input().strip())
n = len(s)

dp = [0] * n
for i in range(1, n): 
    dp[i] = dp[i-1]
    if s[i]==s[i-1]:
        dp[i] += 1


m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(dp[r-1] - dp[l-1])