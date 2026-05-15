import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse = True)
    
    cnt = 0
    team = 0
    for a in A:
        team += 1
        if a * team >= x:
            cnt += 1
            team = 0
            
    print(cnt)