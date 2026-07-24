import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    can = [False] * n
    can[0] = can[-1] = True
    
    INF = 10**9
    left = [INF]*n
    left[0] = A[0]
    for idx, a in enumerate(A[1:], start=1):
        if left[idx-1] >= a:
            can[idx] = True
            left[idx] = a
        else:
            left[idx] = left[idx-1]
            
    right = [-1]*n
    right[-1] = A[-1]
    for idx, a in zip(range(n-2, -1, -1), reversed(A[:-1])):
        if right[idx+1] <= a:
            can[idx] = True
            right[idx] = a
        else:
            right[idx] = right[idx+1]
            
    res = [0]*n
    for idx, x in enumerate(can):
        if x :
            res[idx] = 1
            
    print(*res, sep='')
    
    #print(can)