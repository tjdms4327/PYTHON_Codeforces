import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    res = [A[0]]
    
    min_a = A[0]
    for i in range(1, n):
        min_a = min(min_a, A[i])
        res.append(min_a)
        
    print(sum(res))