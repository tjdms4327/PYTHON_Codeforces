import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    
    cnt = defaultdict(int)
    ans = 0
    
    for _ in range(n):
        s = input().strip()
        
        for c in "abcdefghijk":
            if c != s[0]:
                ans += cnt[c+s[1]]
            if c != s[1]:
                ans += cnt[s[0] + c]

        cnt[s] += 1
        
    print(ans)