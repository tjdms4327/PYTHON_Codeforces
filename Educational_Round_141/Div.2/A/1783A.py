import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    if len(set(A))==1:
        print('NO')
    else:
        print('YES')
        res = sorted(A, reverse=True)
        mx = res[0]
        mx_cnt = res.count(mx)
        if mx_cnt > 1:
            res = res[mx_cnt-1:] + res[:mx_cnt-1]
        
        print(*res)