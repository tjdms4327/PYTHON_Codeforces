import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    mn = min(A)
    mn_cnt = A.count(mn)
    if mn_cnt == n:
        print(-1)
        continue
    
    B = [mn] * mn_cnt
    C = A[mn_cnt:]
    print(mn_cnt, n-mn_cnt)
    print(*B)
    print(*C)