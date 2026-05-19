import sys
input = sys.stdin.readline

n, t = map(int, input().split())
A = list(map(int, input().split()))

l = 0
cur = 0
ans = 0
for r in range(n):
    cur += A[r]
    
    while cur > t:
        cur -= A[l]
        l += 1
    
    ans = max(ans, r-l+1)
    
print(ans)