import sys
input = sys.stdin.readline

def xor_0_to_n(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    x = xor_0_to_n(a - 1)
    if x == b:
        print(a)
    else:
        y = b ^ x
        if y != a:
            print(a+1)
        else:
            print(a+2)