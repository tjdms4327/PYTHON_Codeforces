import sys
input = sys.stdin.readline
from math import gcd

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    pos = [0] * 1001 # 값별 마지막 인덱스
    for i, a in enumerate(A, start=1):
        pos[a] = i
    
    best = -1
    for i in range(1, 1001):
        if pos[i] == 0:
            continue
        for j in range(1, 1001):
            if pos[j] == 0:
                continue
            if gcd(i, j) == 1:
                best = max(best, pos[i] + pos[j])

    print(best)