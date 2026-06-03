import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    one = abs(a-1)
    two = abs(b-c) + abs(c-1)

    if one < two:
        print(1)
    elif one > two:
        print(2)
    else:
        print(3)