n,m,a=map(int, input().split())

from math import ceil
print(ceil(n/a) * ceil(m/a))