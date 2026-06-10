import sys, math
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, x, y, z = map(int, input().split())
    
    no_ai = math.ceil(n/(x+y))
    
    temp = math.ceil(n/x)
    if temp <= z:
        yes_ai = temp
    else:
        yes_ai = z + math.ceil((n-x*z)/(x+10*y))
    
    print(min(no_ai, yes_ai))
