import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip().split('W'))
    

    for cur in s:
        if cur:
            if len(set(cur))!=2:
                print('NO')
                break
    else:
        print('YES')
