import sys
input = sys.stdin.readline
from collections import Counter


n = int(input())
B = list(map(int, input().split()))
B.sort()

cnt = Counter(B)
if B[0]==B[-1]:
    val_cnt = cnt[B[0]]
    print(0, val_cnt*(val_cnt-1)//2)
else:
    min_cnt = cnt[B[0]]
    max_cnt = cnt[B[-1]]
    print(B[-1]-B[0], min_cnt*max_cnt)