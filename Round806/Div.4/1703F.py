import sys
input = sys.stdin.readline
from bisect import bisect_right

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    cand_idx = []
    cand_val = []
    
    for idx, val in enumerate(A, start=1):
        if val < idx:
            cand_idx.append(idx)
            cand_val.append(val)
    cand = sorted(list(zip(cand_idx, cand_val)), key=lambda x:x[1]) # val 기준 정렬
    cand_idx, cand_val = zip(*cand) if cand else([],[])
    
    ans = 0
    m = len(cand_idx)
    for left in range(m):
        i = cand_idx[left]
        
        right = bisect_right(cand_val, i)
        ans += m-right
        
    print(ans)