import sys
input = sys.stdin.readline

n, m = map(int, input().split())
F = list(map(int, input().split()))
F.sort()

best = float('inf')
for i in range(m-n+1):
    best = min(best, F[i+n-1]-F[i])
    
print(best)