import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    length = len(str(n))
    
    ans = 0
    cur_len = 1
    while cur_len < length:
        ans += 9
        cur_len += 1
    
    temp = str(n)[0]
    ans += int(temp) - 1
    if int(temp*length) <= n:
        ans += 1
    
    print(ans)