import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    for i in range(n-2):
        x = A[i]
        A[i] -= x
        A[i+1] -= 2*x
        A[i+2] -= x
        
        if A[i+1]<0 or A[i+2]<0:
            print('NO')
            break
    else:
        if A == [0]*n:
            print('YES')
        else:
            print('NO')