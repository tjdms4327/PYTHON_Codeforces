import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    INF = 10**18
    min_10 = INF
    min_01 = INF
    min_11 = INF
    
    for _ in range(n):
        m, s = input().strip().split()
        m = int(m)
        
        if s == '11':
            min_11 = min(min_11, m)
        elif s == "10":
            min_10 = min(min_10, m)
        elif s == "01":
            min_01 = min(min_01, m)
    
    ans = min(min_11, min_10+min_01)
    if ans >= INF:
        print(-1)
    else:
        print(ans)