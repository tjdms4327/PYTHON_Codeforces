import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = [0] + list(map(int, input().split()))
    
    left, right = 0 , A[1:].count(2)
    for i in range(1, n):
        if A[i]==2:
            left += 1
            right -= 1
            
        if left==right:
            print(i)
            break
    else:
        print(-1)