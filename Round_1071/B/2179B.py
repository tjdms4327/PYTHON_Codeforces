import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
        
    total = 0
    for i in range(1, n):
        total += abs(A[i] - A[i-1])
        
    best = 0
    for i in range(1, n-1):
        gain = (
            abs(A[i-1] - A[i]) +
            abs(A[i] - A[i+1]) -
            abs(A[i-1] - A[i+1])
        )
        best = max(best, gain)
    best = max(best, abs(A[0]-A[1]))
    best = max(best, abs(A[-2]-A[-1]))
        
    print(total-best)