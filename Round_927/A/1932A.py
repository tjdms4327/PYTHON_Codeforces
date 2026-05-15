import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    cur = 0
    coin = [-1]*n
    coin[0] = 0
    for i in range(n):
        if coin[i] == -1:
            continue
        for nxt in (i+1, i+2):
            if nxt<n and s[nxt]!='*':
                gain = 1 if s[nxt]=='@' else 0
                coin[nxt] = max(coin[nxt], coin[i]+gain)

    print(max(coin))