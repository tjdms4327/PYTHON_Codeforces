import sys, math
input = sys.stdin.readline

n, d = map(int, input().split())
B = list(map(int, input().split()))

cnt = 0
for i in range(1, n):
    if B[i] <= B[i-1]:
        diff = -B[i]+B[i-1]+1
        adding = math.ceil(diff/d)
        
        B[i] += d*adding
        cnt += adding
        
print(cnt)