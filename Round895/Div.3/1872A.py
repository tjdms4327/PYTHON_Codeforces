import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    print(math.ceil((abs(a-b)/2)/c))
