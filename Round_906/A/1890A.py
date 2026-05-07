import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = sorted(list(map(int, input().split())))
    
    if len(set(A))==1:
        print('Yes')
    elif len(set(A))==2 and abs(A.count(A[0])-A.count(A[-1])) <= 1:
        print('Yes')
    else:
        print('No')