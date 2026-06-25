import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    
    mx = max(S)
    mx_cnt = S.count(mx)
    
    mx2 = sorted(S)[-2]
    
    res = []
    for i in range(n):
        s = S[i]
        if s < mx:
            res.append(s-mx)
        elif s == mx and mx_cnt>1:
            res.append(0)
        else:
            mx2 = sorted(S)[-2]
            res.append(s-mx2)
            
    print(*res)