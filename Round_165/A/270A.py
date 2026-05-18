import sys
input = sys.stdin.readline

divisors = [180, 2, 90, 3, 60, 4, 45, 
            5, 36, 6, 30, 10, 18, 12, 15]

t = int(input())
for _ in range(t):
    a = int(input())
    
    if 360 % (180-a) == 0:
        print('YES')
    else:
        print('NO')