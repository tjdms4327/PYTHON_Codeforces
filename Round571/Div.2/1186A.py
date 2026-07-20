import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

if min(m, k) >= n:
    print('Yes')
else:
    print('No')