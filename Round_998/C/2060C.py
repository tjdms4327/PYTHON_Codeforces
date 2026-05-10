import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    
    l, r = 0, n-1
    score = 0
    while l < r:
        temp = X[l]+X[r] 
        if temp == k:
            score += 1
            l += 1
            r -= 1
        elif temp < k:
            l += 1
        else:
            r -= 1
            
    print(score)