import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

cand = [
    a*b*c, 
    a*b+c,
    a+b*c,
    a*(b+c),
    (a+b)*c,
    a+b+c
]
print(max(cand))