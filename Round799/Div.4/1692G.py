import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    good = [-1] * (n-1)
    for i in range(n-1):
        if A[i] < 2*A[i+1]:
            good[i] = 0
    
    cur = sum(good[:k])
    ans = 1 if cur==0 else 0
    
    for i in range(1, n-k):
        cur -= good[i-1]
        cur += good[i-1 + k]
        
        if cur==0:
            ans += 1
            
    print(ans)