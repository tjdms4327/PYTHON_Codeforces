import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    max_idx, min_idx = A.index(max(A)), A.index(min(A))
    cand = [
        max(max_idx, min_idx) + 1,
        n - min(max_idx, min_idx),
        min(max_idx, min_idx)+1 + n-max(max_idx, min_idx)
    ]
    print(min(cand))
