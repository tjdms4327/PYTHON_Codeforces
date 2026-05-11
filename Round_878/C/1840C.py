import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    A = list(map(int, input().split()))
    
    l, r = 0, 0
    res = 0
    while r < n:
        if A[r] <= q:
            r += 1
        else:
            if r-l >= k:
                res += (r-l - k + 1)*(r-l - k + 2)//2
            l = r = r+1
    if r-l >= k:
        res += (r-l - k + 1)*(r-l - k + 2)//2
                
    print(res)
    