import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    S = [input().strip() for _ in range(n)]
    
    best_min = 10**9
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            cnt = 0
            cur1, cur2 = S[i], S[j]
            for k in range(m):
                x, y = sorted([cur1[k], cur2[k]])
                cnt += ord(y) - ord(x)
                
            best_min = min(best_min, cnt)
            
    print(best_min)