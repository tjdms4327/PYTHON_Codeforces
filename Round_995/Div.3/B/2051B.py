import sys
input = sys.stdin.readline
from bisect import bisect_left

bl = bisect_left

t = int(input())
for _ in range(t):
    n, a, b, c = map(int, input().split())
    Sum = a+b+c
    
    temp = n//Sum
    cnt = temp * 3
    n -= (n//Sum)*Sum
    
    if n:
        dist = [a, a+b, a+b+c]
        idx = bl(dist, n)
        cnt += (idx+1)
        
    print(cnt)