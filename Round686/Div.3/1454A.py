import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    temp = [i for i in range(1, n+1)]
    ans = temp[1:] + [temp[0]]
    print(*ans)
