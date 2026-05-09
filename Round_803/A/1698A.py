import sys
input = sys.stdin.readline
from functools import reduce

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    print(A[0])