import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    k = math.isqrt(n)
    
    if n != k**2:
        print('No')
        continue
    
    matrix = [s[i*k:(i+1)*k] for i in range(k)]
        
    ok = True
    for r in range(k):
        for c in range(k):
            border = (r == 0 or c == 0 or r == k-1 or c == k-1)

            if border:
                if matrix[r][c] != '1':
                    ok = False
                    break
            else:
                if matrix[r][c] != '0':
                    ok = False
                    break
                
        if not ok:
            break

    print("YES" if ok else "NO")