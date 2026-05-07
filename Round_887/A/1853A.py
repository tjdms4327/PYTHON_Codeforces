import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    if A != sorted(A):
        print(0)
        continue
    
    ans = float('inf')
    for i in range(1, n):
        d = A[i] - A[i-1]
        ans = min(ans, d//2+1)
    print(ans)