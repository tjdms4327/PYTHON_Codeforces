import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
A = [0] + list(map(int, input().split()))

prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1]+A[i]


m = int(input())
questions = list(map(int, input().split()))

for q in questions:
    print(bisect_left(prefix, q))