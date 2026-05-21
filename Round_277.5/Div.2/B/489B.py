import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
B = list(map(int, input().split()))
B.sort()

i, j = 0, 0
cnt = 0

while i<n and j<m:
    if abs(A[i]-B[j]) <= 1:
        cnt += 1
        i += 1
        j += 1
    elif A[i] > B[j]:
        j += 1
    elif A[i] < B[j]:
        i += 1
        
print(cnt)