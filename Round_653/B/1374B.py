import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
        continue
    
    cnt = 0
    while n % 6 == 0:
        n//=6
        cnt += 1
    while n % 3 == 0:
        n //= 3
        cnt += 2
        
    if n == 1:
        print(cnt)
    else:
        print(-1)
        
