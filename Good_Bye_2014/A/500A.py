import sys
input = sys.stdin.readline

n, t = map(int, input().split())
A = list(map(int, input().split()))

cur = 1
while cur < t:
    cur += A[cur-1]
    
if cur==t:
    print('YES')
else:
    print('NO')