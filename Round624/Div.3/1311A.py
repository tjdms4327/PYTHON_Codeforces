import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    if a == b:
        print(0)
    elif a < b:
        diff = b-a
        print(1 if diff%2==1 else 2)
    else:
        diff = a-b
        print(1 if diff%2==0 else 2)
