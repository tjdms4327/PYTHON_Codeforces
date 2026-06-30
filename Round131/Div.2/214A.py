import sys
input = sys.stdin.readline


n, m = map(int, input().split())

cnt = 0
for a in range(m+1):
    b = n - a**2
    if b>=0 and a + b**2 == m:
        cnt += 1
        
print(cnt)