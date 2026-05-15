import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    
    use = n*m - 1
    if use == k:
        print('YES')
    else:
        print('NO')