import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    B = []
    for a in A:
        B.append(n+1-a)
        
    print(*B)