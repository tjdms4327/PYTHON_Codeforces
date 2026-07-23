import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    a, b, c = s.count('A'), s.count('B'), s.count('C')
    if a+c == b:
        print('YES')
    else:
        print('NO')