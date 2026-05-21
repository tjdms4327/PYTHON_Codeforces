import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    P = list(map(int, input().split()))

    suffix_max = [0] * n
    suffix_max[-1] = P[-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], P[i])

    start = -1
    for i in range(n):
        if P[i] < suffix_max[i]:
            start = i
            break

    if start != -1:
        mx = suffix_max[start]
        end = n - 1 - P[::-1].index(mx)
        P[start:end+1] = reversed(P[start:end+1])

    print(*P)
