import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = int(input())
    
    if math.isqrt(s)**2 != s:
        print(-1)
        continue
    
    a_plus_b = math.isqrt(s)
    print(0, a_plus_b)