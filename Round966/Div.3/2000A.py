import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = input().strip()
    
    if len(a) <= 2:
        print('NO')
        continue
    
    front2 = a[:2]
    back = a[2:]
    
    if front2 == '10' and (back[0]!='0' and int(back)>=2):
        print('YES')
    else:
        print('NO')
