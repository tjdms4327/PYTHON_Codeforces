import sys
input = sys.stdin.readline
import math

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    A[0] += 1
    print(math.prod(A))