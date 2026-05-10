import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, x, y = map(int, input().split())
    
    
    if a-b >= 2:
        print(-1)
        continue
    elif a-b == 1:
        if a%2==1:
            print(y)
        else:
            print(-1)
        continue
    elif a == b:
        print(0)
        continue
    
    
    res = 0
    cur = a
    while cur != b:
        if cur % 2 == 0:
            res += min(x, y)
        else:
            res += x
        cur += 1
    print(res)