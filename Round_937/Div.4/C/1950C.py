import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, m = map(int, input().split(':'))
    
    ampm = 'AM'
    if h == 0:
        h = 12
    elif h == 12:
        ampm = 'PM'
    elif h > 12:
        h -= 12
        ampm = 'PM'
        
    print(f'{h:02d}:{m:02d} {ampm}')