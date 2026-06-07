import sys
input = sys.stdin.readline

def fair_num(num):
    cand = set(map(int, str(num)))
    for c in cand:
        if c>0 and num%c != 0:
            return False
    else:
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    
    x = n
    while not fair_num(x):
        x += 1
    
    print(x)