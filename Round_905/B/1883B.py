import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = Counter(list(input().strip()))
    
    odd = sum(v % 2 for v in s.values())
    
    if k >= odd-1:
        print('YES')
    else:
        print('NO')