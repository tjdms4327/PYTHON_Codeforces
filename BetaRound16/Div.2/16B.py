import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cnt = []
for _ in range(m):
    a, b = map(int, input().split())
    cnt.append([b, a])
cnt.sort(reverse=True)

ans = 0
for b, a in cnt:
    if n >= a:
        ans += a*b
    else:
        ans += b*n
        break
    
    n -= a
    
print(ans)

