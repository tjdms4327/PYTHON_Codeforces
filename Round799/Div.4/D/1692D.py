import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s, x = input().strip().split()
    x = int(x)
    
    h, m = map(int, s.split(':'))
    cur = 60*h+m
    
    time = set()
    cnt = 0
    while True:
        cur %= (24*60)
        hh = cur // 60
        mm = cur % 60
        hm = f"{hh:02d}{mm:02d}"
        
        if hm in time:
            break
        time.add(hm)
        
        if hm == hm[::-1]:
            cnt += 1
        
        
        cur += x
        

    print(cnt)