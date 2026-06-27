import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    c = input().strip()
    
    if c in 'codeforces':
        print('YES')
    else: print('NO')