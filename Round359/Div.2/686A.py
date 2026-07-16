import sys
input = sys.stdin.readline

n, icecream = map(int, input().split())

disappoint = 0
for _ in range(n):
    c, d = input().strip().split()
    d = int(d)
    
    if c == '+':
        icecream += d
    else:
        if icecream >= d:
            icecream -= d
        else:
            disappoint += 1
            
print(icecream, disappoint)
