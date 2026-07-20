import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    prev = [0]*(n+1)
    for i in range(1, n+1):
        prev[i] = prev[i-1] + A[i-1]
    
    best = -1
    for i in range(1, n+1):
        for j in range(i):
            best = max(best, (prev[i]-prev[j])//(i-j))
    print(best)            