import sys
input = sys.stdin.readline
from collections import deque

s = input().strip()

target = "hello"
i = 0
for cur in s:
    if cur == target[i]:
        i += 1
        if i == len(target):
            break

if i == len(target):
    print('YES')
else:
    print('NO')
