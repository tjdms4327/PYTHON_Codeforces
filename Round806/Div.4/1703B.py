import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    p = set()
    ballon = 0
    for x in s:
        ballon += 1
        if x not in p:
            p.add(x)
            ballon += 1
    
    print(ballon)