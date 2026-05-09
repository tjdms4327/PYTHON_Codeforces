import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + A[i]
    total = prefix[n]
    
    for _ in range(q):
        l, r, k = map(int, input().split())
        
        segment = prefix[r] - prefix[l-1]
        res = total - segment + k*(r-l+1)
        
        if res%2==1:
            print('YES')
        else:
            print('NO')