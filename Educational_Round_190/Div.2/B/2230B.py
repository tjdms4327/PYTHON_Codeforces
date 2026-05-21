import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = list(input().strip())
    n = len(s)
   
    suf = [0] * (n+1) # i 이후의 1, 3 개수
    for i in range(n-1, -1, -1):
        suf[i] = suf[i+1]
        if s[i] in '13':
            suf[i] += 1
            
    ans = 0
    twos = 0
    # i 기준 왼쪽은 2, 오른쪽은 13만 남김
    for i in range(n+1):
        ans = max(ans, twos+suf[i]) # 남길 수 있는 길이
        if i<n and s[i]=='2':
            twos += 1
            
    print(n-ans)
