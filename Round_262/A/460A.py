import sys
input = sys.stdin.readline

n, m = map(int, input().split())

days = 0
while n:
    if n >= m:
        days += m
        n = n - m + 1
    else:
        days += n
        break
    
print(days)