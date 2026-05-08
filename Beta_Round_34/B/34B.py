import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

res = 0
for i in range(m):
    a = A[i]
    if a<0:
        res -= a
    else:
        break
    
print(res)
