import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    S = input().strip()
    
    s = S.index('B')
    e = S.rindex('B')
    print(e-s+1)    