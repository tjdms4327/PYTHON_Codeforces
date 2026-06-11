import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    alice, bob = [A[0]], []
    moves = 1
    
    l, r = 1, n-1
    while l <= r:
        if moves%2: # 이번이 Bob 차례
            past = alice[-1]
            cur = 0
            while cur <= past and l<=r:
                cur += A[r]
                r -= 1
                
            bob.append(cur)
        
        else: # alice 차례
            past = bob[-1]
            cur = 0
            while cur <= past and l<=r:
                cur += A[l]
                l += 1
                
            alice.append(cur)
            
        moves += 1
    
    print(moves, sum(alice), sum(bob))