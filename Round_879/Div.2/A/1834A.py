import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    pos = sum(1 for x in A if x == 1)
    neg = n - pos

    cnt = 0

    while neg > pos:
        neg -= 1
        pos += 1
        cnt += 1
    if neg % 2:
        cnt += 1

    print(cnt)