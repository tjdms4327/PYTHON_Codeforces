import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

Max = 0
for l in range(n):
    for r in range(l, n):
        B = A[:l] + A[r+1:]
        C = A[l:r+1]
        Max = max(Max, B.count(1)+C.count(0))
        
print(Max)