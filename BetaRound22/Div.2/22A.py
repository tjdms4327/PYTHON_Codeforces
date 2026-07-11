import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))

sorted_A = sorted(list(A))
if len(sorted_A) < 2:
    print('NO')
else:
    print(sorted_A[1])