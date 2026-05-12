import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    s.sort()
    
    print(ord(s[-1])-ord('a')+1)
    