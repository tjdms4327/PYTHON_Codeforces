import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()
    
    ok = 'YES'
    for i in range(n):
        if s1[i]==s2[i]=='R':
            continue
        elif s1[i]=='R' or s2[i]=='R':
            ok = 'NO'
            break
        else:
            continue
        
    print(ok)