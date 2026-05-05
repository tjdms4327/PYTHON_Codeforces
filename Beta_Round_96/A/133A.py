import sys
input = sys.stdin.readline

s = input().strip()
if any(x in s for x in 'HQ9'):
    print('YES')
else:
    print('NO')