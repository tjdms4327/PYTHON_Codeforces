import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    b.sort()
    total = Counter(b)
    
    x = b[-1]
    
    ok = False
    
    # y 후보는 전부 시도 (n ≤ 100이라 가능)
    for i in range(n):
        if i == n - 1:
            continue
        
        cnt = total.copy()
        y = b[i]
        
        cnt[x] -= 1
        cnt[y] -= 1
        
        a, b_ = x, y
        valid = True
        
        for _ in range(n - 2):
            if b_ == 0:
                valid = False
                break
            
            z = a % b_
            
            if cnt[z] == 0:
                valid = False
                break
            
            cnt[z] -= 1
            a, b_ = b_, z
        
        if valid:
            print(x, y)
            ok = True
            break
    
    if not ok:
        print(-1)