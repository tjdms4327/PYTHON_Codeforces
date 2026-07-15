import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

for i in range(n):
    print(A[i], A[2*n-1-i])
