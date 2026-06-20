import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    ai = max(A)
    mx_indices = [idx for idx, val in enumerate(A) if val==ai]
    
    res = ai+1
    for i in mx_indices:
        left, right = A[:i-1], A[i+2:]
        
        left_cnt = (len(left)+1)//2
        if i in [0, 1]:
            left_cnt = 0
        right_cnt = (len(right)+1)//2
        if i in [n-2, n-1]:
            right_cnt = 0
        
        res = max(res, ai+left_cnt+right_cnt+1)

    print(res)
    