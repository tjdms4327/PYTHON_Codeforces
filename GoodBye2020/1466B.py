import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    X = list(map(int, input().split()))
    
    visited = [False]*(2*n+3)
    for x in X:
        if visited[x]:
            visited[x+1] = True
        else:
            visited[x] = True
        
    
    print(sum(visited))