import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    cnt = list(map(int, input().split()))
    
    if any(x>=3 for x in cnt):
        print('YES')
    elif sum(x>=2 for x in cnt) >= 2:
        print('YES')
    else:
        print('NO')