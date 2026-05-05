import sys
input = sys.stdin.readline

s = input().strip()

org = s.split('WUB')
print(' '.join(x for x in org if x))