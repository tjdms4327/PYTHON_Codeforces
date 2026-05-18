import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    
    right = [0]*(n+1)
    seen = set()
    for i in range(n-1, -1, -1):
        seen.add(s[i])
        right[i] = len(seen)
    
    best = -1
    seen.clear()
    for i in range(n-1):
        seen.add(s[i])
        
        best = max(best, len(seen) + right[i+1])
    
    print(best)
    