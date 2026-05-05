import sys
input = sys.stdin.readline

n, k = map(int, input().split())

odd_cnt = (n+1) // 2
if k <= odd_cnt:
    print(2*k-1)
else:
    print(2*(k-odd_cnt))