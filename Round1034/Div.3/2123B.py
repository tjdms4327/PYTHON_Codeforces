import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, j, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    if A[j-1] == max(A):
        print('YES')
    else:
        if k >= 2:
            print('YES')
        else:
            print('NO')