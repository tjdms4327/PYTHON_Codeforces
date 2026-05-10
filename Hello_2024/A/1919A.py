import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a==b:
        print('Bob')
    else:
        rest = abs(b-a)
        if rest%2:
            print('Alice')
        else:
            print('Bob')