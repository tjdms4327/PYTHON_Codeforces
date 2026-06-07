import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, x, y, n = map(int, input().split())
    
    # case 1) a 먼저 깎기
    a1, b1 = a, b
    minus = min(n, a1-x)
    a1 -= minus
    rem = n-minus
    b1 -= min(rem, b1-y)

    # case 2) b 깎기
    a2, b2 = a, b
    minus = min(n, b2-y)
    b2 -= minus
    rem = n-minus
    a2 -= min(rem, a2-x)

    print(min(a1*b1, a2*b2))
