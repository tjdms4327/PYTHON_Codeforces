import sys
input = sys.stdin.readline

INF = float('inf')

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    
    ans = INF
    
    for x in range(min(A), max(A)+1):
        diff = [abs(ai-x) for ai in A]
        ans = min(ans, max(diff))
        
    print(ans)