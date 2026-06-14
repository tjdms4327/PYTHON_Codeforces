import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    slice1, slice2 = [],[]
    for i in range(n):
        if i%2:
            slice1.append(A[i])
        else:
            slice2.append(A[i])
    

    if (all(x%2 for x in slice1) and all(x%2 for x in slice2)) \
        or (all(x%2==0 for x in slice1) and all(x%2 for x in slice2))\
        or (all(x%2 for x in slice1) and all(x%2==0 for x in slice2))\
        or (all(x%2==0 for x in slice1) and all(x%2==0 for x in slice2)):
            print('YES')
    else:
        print('NO')
