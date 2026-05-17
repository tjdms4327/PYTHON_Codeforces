import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = list(input().strip())
    n = len(s)
    
    one = s.count('1')
    zero = n - one
    
    ans = 0
    for c in s:
        if c == '0':
            if one == 0:
                break
            one -= 1
      
        else:
            if zero == 0:
                break
            zero -= 1
        
        ans += 1
    
    print(n - ans)      