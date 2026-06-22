import sys
input = sys.stdin.readline
from bisect import bisect_right
br = bisect_right

t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    if l==r and d==u and l+r==d+u:
        print('YES')
    else:
        print('NO')