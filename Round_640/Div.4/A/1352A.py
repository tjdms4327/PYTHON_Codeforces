import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = list(map(int, input().strip()))

    result = []
    l = len(n)
    for i in range(l):
        if n[i] != 0:
            temp = n[i]*(10**(l-1-i))
            result.append(temp)
    print(len(result))
    print(*result)
        