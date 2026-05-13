import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    x, y = 0,0
    for ch in s:
        if ch=='U':
            y += 1
        elif ch == 'D':
            y -= 1
        elif ch=='R':
            x += 1
        elif ch=='L':
            x -= 1
            
        if (x, y)==(1,1):
            print('YES')
            break
    else:
        print('NO')
    