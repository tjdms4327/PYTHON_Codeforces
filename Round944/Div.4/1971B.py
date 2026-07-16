import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = list(input().strip())
    if len(set(s))==1:
        print('NO')
    else:
        print('YES')
        
        new = sorted(s)
        if new == s:
            new = new[::-1]
        print(''.join(new))
        