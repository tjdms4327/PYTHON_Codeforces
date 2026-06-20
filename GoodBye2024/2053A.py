import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    for i in range(1,n):
        Min, Max = min(A[i],A[i-1]), max(A[i],A[i-1])
        if 2*Min > Max:
            print('YES')
            break
    else:
        print('NO')
                
            