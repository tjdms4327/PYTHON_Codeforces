import sys
input = sys.stdin.readline

n = int(input())
    
if n % 2:
    print(0)
else:
    k = n // 2
    print(2**k)