import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    S = list(map(int, input().split()))
    cand = [max(S[:2]), max(S[2:])]
    
    S.sort()
    if sorted([S[-1], S[-2]]) == sorted(cand):
        print('YES')
    else:
        print('NO')