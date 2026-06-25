import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    cur = 0
    res = []
    used = [False] * n
    
    for _ in range(min(31, n)):
        best = -1
        idx = -1

        for i in range(n):
            if not used[i]:
                val = cur | A[i]

                if val > best:
                    best = val
                    idx = i

        if best == cur:
            break

        res.append(A[idx])
        used[idx] = True
        cur = best
    
    
    for i in range(n):
        if not used[i]:
            res.append(A[i])
    
    print(*res)