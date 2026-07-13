import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(input().strip())
    
    for r in range(k):
        cnt = 0
        for i in range(r, n, k):
            cnt += (s[i]=='1')
            
        # 해당 r에 대해
        if cnt % 2:
            print('NO')
            break
    else:
        print('YES')