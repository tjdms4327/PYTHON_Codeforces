import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    line = list(map(int, input().split()))
    if sum(line) == 2*max(line):
        print('YES')
    else:
        print('NO')