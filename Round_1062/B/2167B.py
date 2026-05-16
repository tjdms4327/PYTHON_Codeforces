import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    n = int(input())
    s, t = input().strip().split()
    
    if sorted(s) == sorted(t):
        print('YES')
    else:
        print('NO')