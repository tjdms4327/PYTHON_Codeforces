import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    cnt = s[:k].count('W')
    best = cnt
    
    l, r = 0, k
    while r < n:
        if s[l]=='W':
            cnt -= 1
        l += 1
    
        
        if s[r] == 'W':
            cnt += 1
        r += 1
        
        best = min(best, cnt)
        
    print(best)