import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    even = sum(1 for a in A if a%2==0)
    if k == 2:
        if even:
            print(0)
        else:
            print(1)
    elif k == 4:
        if even >= 2:
            print(0)
        elif any(a%4==0 for a in A):
            print(0)
        else:
            make4 = min((4 - a % 4) % 4 for a in A)
            make2 = 1 if even==1 else 2
            print(min(make4, make2))
    elif k==3:
        if any(a%3==0 for a in A):
            print(0)
        else:
            print(min(3-a%3 for a in A))
    elif k == 5:
        if any(a%5==0 for a in A):
            print(0)
        else:
            print(min(5-a%5 for a in A))