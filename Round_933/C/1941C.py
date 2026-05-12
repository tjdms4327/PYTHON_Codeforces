import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if 'pie' not in s and 'map' not in s:
        print(0)
        continue
    
    cnt = 0
    i = 0
    while i < n:
        if s[i:i+5] == 'mapie':
            cnt += 1
            i += 5
        elif s[i:i+3] in ['map', 'pie']:
            cnt += 1
            i += 3
        else:
            i += 1
            
    print(cnt)