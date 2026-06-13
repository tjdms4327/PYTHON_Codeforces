import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    W = list(map(int, input().split()))

    l, r = 0, n-1
    alice, bob = 0, 0
    best = 0
    while l<=r:
        if alice <= bob:
            alice += W[l]
            l += 1
        else:
            bob += W[r]
            r -= 1
        
        if alice == bob:
            best = max(best, l+(n-r-1))
            
    print(best)