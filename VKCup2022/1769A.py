import sys
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]

ans = [-1]*(n+1)
ans[1] = A[0] - 1
for i in range(2, n+1):
    ans[i] = max(ans[i-1]+1, A[i-1]-i)
    
print(*ans[1:], sep='\n')
