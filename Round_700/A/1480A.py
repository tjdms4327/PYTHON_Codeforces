import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    res = ''
    i = 0
    while len(s) != len(res):
        if i%2==0:
            if s[i]=='a':
                res += 'b'
            else:
                res += 'a'
        else:
            if s[i] =='z':
                res += 'y'
            else:
                res += 'z'
        
        i += 1        
        
    print(res)