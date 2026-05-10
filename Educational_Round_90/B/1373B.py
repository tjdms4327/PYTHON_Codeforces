import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    poss = min(s.count('1'), s.count('0'))
    if poss % 2:
        print('DA')
    else:
        print('NET')