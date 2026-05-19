import sys
input = sys.stdin.readline

n, m, a, b = map(int, input().split())

if b >= m*a:
    print(n*a)
else:
    special = (n//m)*b
    print(special + min(b, (n%m)*a))