import sys
input = sys.stdin.readline

n, l = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

diff = 0
for i in range(1, n):
    temp = A[i] - A[i-1]
    diff = max(diff, temp/2)

diff = max(diff, A[0], l-A[-1])
print(diff)