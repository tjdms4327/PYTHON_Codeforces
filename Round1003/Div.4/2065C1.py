import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    b = int(input())
    
    if n == 1:
        print('YES')
        continue
    
    changed = [b-a for a in A]
    
    prev = min(A[0], changed[0])
    for i in range(1,n):
        x1 = min(A[i], changed[i])
        x2 = max(A[i], changed[i])
        if x1 >= prev:
            prev = x1
        elif x2 >= prev:
            prev = x2
        else:
            print('NO')
            break
    else:
        print('YES')