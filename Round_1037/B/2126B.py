import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    cnt = 0
    dp = [0]*(n)
    dp[0] = 1 if A[0]==0 else 0
    for i in range(1, n):
        if A[i]==0:
            dp[i] = dp[i-1] + 1
        else:
            cnt += (dp[i-1]+1)//(k+1)
    if dp[-1]:
        cnt += (dp[-1]+1)//(k+1)
    
    #print(dp)
    print(cnt)