import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

tot = sum(A)

prefix = 0
cnt = 0
for i in range(n-1):
    prefix += A[i]
    if prefix * 2 == tot:
        cnt += 1
        
print(cnt)