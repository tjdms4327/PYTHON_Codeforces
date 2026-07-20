import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    
    continuous = False
    for i in range(n-1):
        if s[i] == s[i+1]:
            continuous = True
            break
        
    if continuous:
        print(1)
    else:
        print(n)