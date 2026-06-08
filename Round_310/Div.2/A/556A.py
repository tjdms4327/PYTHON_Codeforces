import sys
input = sys.stdin.readline

t = int(input())
s = input().strip()

delete = min(s.count('0'), s.count('1'))
print(t - 2*delete)
