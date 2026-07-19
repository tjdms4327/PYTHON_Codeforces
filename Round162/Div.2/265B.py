import sys
input = sys.stdin.readline

n = int(input())
H = [int(input()) for _ in range(n)]

time = H[0] + 1
for i in range(1, n):
    if H[i-1] <= H[i]:
        time += 1 - H[i-1] + H[i]
    else:
        time += 1 + H[i-1] - H[i]
        
    time += 1 # 견과류 먹기

print(time)