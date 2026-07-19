import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    possible = ['abc', 'acb', 'cba', 'bac']
    if s in possible:
        print('YES')
    else:
        print('NO')