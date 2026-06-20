import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = input().strip()

cnt = [0] * n
for i in range(n):
    x = s[i]
    cnt[i] = ord(x)-ord('a')+1
    
prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + cnt[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r]-prefix[l-1])