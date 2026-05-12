import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())
    
    temp = (a+b+c+n)//3
    if (a+b+c+n)%3==0 and (temp>=max(a, b, c)):
        print('YES')
    else:
        print('NO')