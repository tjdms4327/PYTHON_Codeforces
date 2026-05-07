import sys
input = sys.stdin.readline

n = int(input())

cand = [2]*(n//2)
if n % 2 == 1:
    cand[-1] += 1
    
print(len(cand))
print(*cand)