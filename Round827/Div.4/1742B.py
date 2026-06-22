import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    if len(set(A))==n:
        print('YES')
    else:
        print('NO')