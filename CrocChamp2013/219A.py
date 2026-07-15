import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
IDs = list(map(int, input().split()))

cnt = Counter(IDs)
if any(val>2 for key, val in cnt.items() if key!=0):
    print(-1)
else:
    print(sum(val==2 for key, val in cnt.items() if key!=0))
