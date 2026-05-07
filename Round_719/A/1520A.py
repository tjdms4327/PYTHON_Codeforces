import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    already = set(s[0])
    for i in range(1, n):
        if s[i-1]==s[i]:
            continue
        else:
            if s[i] not in already: 
                already.add(s[i])
            else:
                print('NO')
                break
    else:
        print('YES') 