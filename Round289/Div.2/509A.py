import sys
input = sys.stdin.readline

dp = [[1]*11 for _ in range(11)]
for i in range(2, 11):
    for j in range(2, 11):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


n = int(input())
print(dp[n][n])
