import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(-1)
    sys.exit()
    
if n%2:
    print(-1)
else:
    res = [x for i in range(1, n, 2) for x in (i+1, i)]
    print(*res)