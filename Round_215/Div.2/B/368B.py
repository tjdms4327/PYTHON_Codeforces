import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [0]*n
seen = set()
for i in range(n-1,-1,-1):
    seen.add(A[i])
    dp[i] = len(seen)
        
for _ in range(m):
    l = int(input())
    print(dp[l-1])
    