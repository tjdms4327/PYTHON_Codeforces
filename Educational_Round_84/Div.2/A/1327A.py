import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    if n >= k**2 and (n-k**2)%2==0:
        print('YES')
    else:
        print('NO')