import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    lst = [a%3 for a in A]
    
    r = sum(A) % 3
    if n == 1:
        if r == 0:
            print(0)
        else:
            print(1)
        continue
    
    if r == 0:
        print(0)
    elif r == 2:
        print(1)
    else: # r==1
        if 1 in lst:
            print(1)
        else:
            print(2)