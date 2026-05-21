import sys
input = sys.stdin.readline

n = int(input())
V = list(map(int, input().split()))

prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + V[i-1]

sorted_V = sorted(V)
sorted_prefix = [0] * (n+1)
for i in range(1, n+1):
    sorted_prefix[i] = sorted_prefix[i-1] + sorted_V[i-1]


m = int(input())
for _ in range(m):
    type, l, r = map(int, input().split())
    
    if type == 1:
        print(prefix[r] - prefix[l-1])
    elif type == 2:
       print(sorted_prefix[r] - sorted_prefix[l-1]) 