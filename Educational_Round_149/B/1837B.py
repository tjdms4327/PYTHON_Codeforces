import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    
    ans = 0
    cur = 1
    for i in range(1, n):
        if s[i]==s[i-1]:
            cur += 1
        else:
            ans = max(ans, cur)
            cur = 1
    ans = max(ans, cur)
    
    print(ans+1)