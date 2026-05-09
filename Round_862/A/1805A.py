import sys
input = sys.stdin.readline
from functools import reduce

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    a_res = reduce(lambda x, y:x^y, A)
    x_cnt = n%2
    if x_cnt==0:
        if a_res==0:
            print(0)
        else:
            print(-1)
    else:
        print(a_res)