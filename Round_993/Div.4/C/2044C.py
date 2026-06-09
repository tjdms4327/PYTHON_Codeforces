import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, a, b, c = map(int, input().split())
    
    row1 = min(m, a)
    row2 = min(m, b)
    
    ans = row1+row2
    if row1 < m:
        temp = min(m - row1, c)
        ans += temp
        c -= temp
    if row2 < m:
        temp = min(m - row2, c)
        ans += temp
        c -= temp

    print(ans)        