import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    if k%2==0:
        if n%2:
            print('NO')
        else:
            print('YES')
    else: #k가 홀수
        print('YES')