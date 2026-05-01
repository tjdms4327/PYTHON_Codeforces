import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    if A[i] > A[i-1]:
        dp[i] = dp[i-1]+1

print(max(dp))
