import sys
input = sys.stdin.readline
from math import ceil

n = int(input())
S = list(map(int, input().split()))

cnt = S.count(4)
one, two, three = S.count(1), S.count(2), S.count(3)

cnt += two//2
if two % 2==1:
    one -= min(2, one)
    cnt += 1

pair = min(one, three)
cnt += pair
one -= pair
three -= pair
if three:
    cnt += three
if one:
    cnt += ceil(one/4)
    
print(cnt)