import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
goals = Counter([input().strip() for _ in range(n)])


print(goals.most_common(1)[0][0])