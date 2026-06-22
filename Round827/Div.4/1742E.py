import sys
input = sys.stdin.readline
from bisect import bisect_right
br = bisect_right

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    K = list(map(int, input().split()))
    
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + A[i-1]
    
    queries = sorted([(K[i], i) for i in range(q)])

    ans = [0] * q
    j = 0
    for k, idx in queries:
        while j < n and A[j] <= k:
            j += 1
        ans[idx] = prefix[j]

    print(*ans)