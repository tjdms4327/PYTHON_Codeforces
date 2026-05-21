import sys
input = sys.stdin.readline

n, k = map(int, input().split())

time = 4*60 - k
result = n
for i in range(1, 1+n):
    if time >= 5*i:
        time -= 5*i
    else:
        result = i-1
        break
    
print(result)
