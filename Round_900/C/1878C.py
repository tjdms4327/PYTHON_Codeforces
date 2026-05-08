import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    if k*(k+1)//2 <= x <= k*(2*n-k+1)//2:
        print('YES')
    else:
        print('NO')