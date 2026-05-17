import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

best = 10**5
for a in A:
    best = min(best, abs(a))
    
print(best)