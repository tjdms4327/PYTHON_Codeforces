import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    enemy = list(map(int, input().strip()))
    gregor = list(map(int, input().strip()))
    
    ans = 0
    for i in range(n):
        if gregor[i] == 0:
            continue
        
        # 왼쪽 적 먹기
        if i>0 and enemy[i-1]==1:
            enemy[i-1] = 2 # gregor가 자리 차지
            ans += 1
        # 직진
        elif enemy[i] == 0:
            ans += 1
        # 오른쪽 적 먹기
        elif i<n-1 and enemy[i+1]==1:
            enemy[i+1] = 2
            ans += 1
        
    print(ans)