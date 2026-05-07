import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    cand = [0,0]
    for x in range(2, n+1):
        k = n//x
        temp = x*(k+1)*k//2
        if cand[-1] <= temp:
            cand = [x, temp]
            
    print(cand[0])