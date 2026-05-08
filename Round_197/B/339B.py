import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

cur = 1
res = 0
for nxt in A:
    if nxt > cur:
        res += nxt-cur
    elif nxt < cur:
        res += (n-cur)+nxt
    cur = nxt
        
print(res)