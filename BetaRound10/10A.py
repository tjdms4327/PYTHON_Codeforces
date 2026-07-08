import sys
input = sys.stdin.readline

n, p1, p2, p3, t1, t2 = map(int, input().split())

times = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    l, r = times[i]
    ans += (r-l)*p1
    
    if i < n-1:
        nxt = times[i+1][0]
        if t2+t1+r <= nxt:
            ans += (nxt-(t2+t1+r))*p3
            ans += p2*t2
            ans += p1 * t1
        elif t1+r <= nxt:
            ans += (nxt-(t1+r))*p2
            ans += p1*t1
        else:
            ans += (nxt-r)*p1
            
print(ans)