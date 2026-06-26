import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split()))
    
    inv = 0
    one = 0
    for x in A:
        if x == 1:
            one += 1
        else:
            inv += one
    
    one_before = 0
    zero_after = A.count(0)
    best = 0
    for i in range(n):
        if A[i]==0:
            zero_after -= 1
            delta = zero_after - one_before
            best = max(best, delta)
        else:
            delta = one_before - zero_after
            best = max(best, delta)
            one_before += 1
            
    print(inv+best)