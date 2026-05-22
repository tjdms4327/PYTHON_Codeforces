import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
     
    A = [i for i in range(1, 2*n+1, 2)]
    print(*A)
