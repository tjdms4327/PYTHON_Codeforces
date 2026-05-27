import sys
input = sys.stdin.readline
from bisect import bisect_right


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B.sort
    C.sort()
    
    cnt = 0
    for b in B:
        idx = bisect_right(C, k-b)
        cnt += idx
        
    print(cnt)