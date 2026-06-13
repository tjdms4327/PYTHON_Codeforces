import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    cnt = {}
    for x in A:
        cnt[x] = cnt.get(x, 0) + 1
        if cnt[x] == 3:
            print(x)
            break
    else:
        print(-1)
