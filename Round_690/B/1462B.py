import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if s[:4]=='2020' or s[:3]+s[-1]=='2020' \
        or s[:2]+s[-2:]=='2020' or s[0]+s[-3:]=='2020'\
        or s[-4:]=='2020':
            print('YES')
    else:
        print('NO')