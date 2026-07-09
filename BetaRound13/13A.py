import sys
input = sys.stdin.readline

A = int(input())

tot = 0
for i in range(2, A):
    x = A
    while x:
        tot += x%i
        x //= i
        

from math import gcd
g = gcd(tot, A-2) # 최대공약수
print(f'{tot//g}/{(A-2)//g}')
