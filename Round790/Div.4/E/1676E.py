import sys
input = sys.stdin.readline
from bisect import bisect_left

bl = bisect_left

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + A[i-1]
    

    for _ in range(q):
        x = int(input())
        
        if x > prefix[-1]:
            print(-1)
            continue
            
        cnt = bl(prefix, x)
        print(cnt)