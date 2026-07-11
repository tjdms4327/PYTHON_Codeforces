import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

half = sum(A) / 2

prefix = [0]*n
prefix[0] = A[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + A[i]
    
cnt = 0
for i in range(n-1):
    if prefix[i] == half:
        cnt += 1
        
print(cnt)