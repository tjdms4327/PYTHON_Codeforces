import sys, math
input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))

for x in X:
    if math.isqrt(x)**2 != x:
        print('no')
    else:
        print('yes')