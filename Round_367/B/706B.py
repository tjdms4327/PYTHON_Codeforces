import sys
input = sys.stdin.readline
from bisect import bisect_right

n = int(input())
X = list(map(int, input().split()))
X.sort()

q = int(input())
for _ in range(q):
    m = int(input())
    cnt = bisect_right(X, m) # m이 들어갈 가장 오른쪽 위치
    print(cnt)
