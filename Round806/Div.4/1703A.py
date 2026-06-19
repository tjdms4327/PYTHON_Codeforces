import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip().upper()
    
    if s == 'YES':
        print('YES')
    else:
        print('NO')