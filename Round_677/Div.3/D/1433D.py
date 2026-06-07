import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    diff_first = 0
    for idx, a in enumerate(A[1:], start=1):
        if A[0] != a:
            diff_first = idx
            break
    
    if diff_first == 0:
        print('NO')
        continue
    
    root = A[0]
    
    res = []
    for idx, a in enumerate(A[1:], start=1):
        if root != a:
            res.append((1, idx+1)) # 1-based
        else:
            res.append((diff_first+1, idx+1))
        
    print('YES')
    for row in res:
        print(*row)