import sys
input = sys.stdin.readline

n, k = map(int, input().split())
H = list(map(int, input().split()))

dp = [0]*(n-k+1)
dp[0] = sum(H[:k])
for i in range(1, n-k+1):
    dp[i] = dp[i-1]-H[i-1]+H[i+k-1]
    
print(dp.index(min(dp))+1)