import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))


count = 0
Min, Max = A[0], A[0]
for a in A[1:]:
    if a<Min:
        count += 1
        Min = a
    elif a>Max:
        count += 1
        Max = a
print(count)
