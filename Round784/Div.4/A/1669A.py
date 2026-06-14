import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    rating = int(input())
    
    if rating >= 1900:
        d = 1
    elif rating >= 1600:
        d = 2
    elif rating >= 1400:
        d = 3
    else:
        d = 4
        
    print(f'Division {d}')
