import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    if d < b:
        print(-1)
        continue
    
    cnt = d - b
    a += cnt
    if a < c:
        print(-1)
        continue
    else:
        temp = a - c
        cnt += temp
        
    print(cnt)
    
