import sys
input = sys.stdin.readline

n, t = map(int, input().split())

houses = []
for _ in range(n):
    x, a = map(int, input().split())
    houses.append((x-a/2, x+a/2))
houses.sort()

cnt = 1+1 # 맨 왼쪽, 맨 오른쪽
for i in range(len(houses)-1):
    l, r = houses[i]
    nxr_l, _ = houses[i+1]
    
    diff = nxr_l - r
    if diff == t:
        cnt += 1
    elif diff > t:
        cnt += 2
        
print(cnt)