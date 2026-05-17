import sys
input = sys.stdin.readline

n, m = map(int, input().split())

Min = (n+1)//2
Max = n

for x in range(Min, Max+1):
    if x%m==0:
        print(x)
        break
else:
    print(-1)