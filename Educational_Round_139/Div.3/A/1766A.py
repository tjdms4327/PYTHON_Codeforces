import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    x = 1
    cnt = 0
    while x < len(str(n)):
        cnt += 9
        x += 1
        
    cnt += int(str(n)[0])
    print(cnt)