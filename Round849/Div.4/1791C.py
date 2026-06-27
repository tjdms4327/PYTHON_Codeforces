import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    while len(s) > 0 and s[0] != s[-1]:
        s = s[1:-1]
        
    print(len(s))
