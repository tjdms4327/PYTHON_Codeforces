import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    ok = False
    for i in range(2, math.isqrt(n)+1):
        if n%i == 0:
            a = i
            left = n//i
            for j in range(2, math.isqrt(left)+1):
                if left%j == 0:
                    b = j
                    c = left//j
                    if (a!=b and b!= c and a!= c) and c >= 2:
                        print('YES')
                        print(a, b, c)
                        ok = True
                        break
        if ok:
            break
                        
    else:
        print('NO')