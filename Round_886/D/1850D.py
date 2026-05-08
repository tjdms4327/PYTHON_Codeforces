import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    dp = [1] *(n+1)
    for i in range(1, n):
        if A[i]-A[i-1] <= k:
            dp[i] = dp[i-1] + 1
            
    print(n-max(dp))