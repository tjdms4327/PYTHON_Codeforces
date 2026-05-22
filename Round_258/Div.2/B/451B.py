import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

if A == sorted(A):
    print('yes')
    print(1, 1)
    sys.exit()
elif A == sorted(A, reverse=True):
    print('yes')
    print(1, n)
    sys.exit()

sorted_A = sorted(A)
l, r = 0, n-1
while l<n and A[l]==sorted_A[l]:
    l += 1
while l<=r and A[r]==sorted_A[r]:
    r -= 1

if A[l:r+1][::-1] == sorted(A[l:r+1]):
    print('yes')
    print(l+1, r+1)
else:
    print('no')