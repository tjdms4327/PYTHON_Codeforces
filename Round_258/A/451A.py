import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = min(n, m)%2
if res:
    print('Akshat')
else:
    print('Malvika')