import sys, math
input = sys.stdin.readline

n, x = map(int, input().split())
    
cand = set()
for i in range(1, n+1):
    if x%i==0:
        if i <= n and x//i <= n:
            cand.add((i, n//i))
print(len(cand))