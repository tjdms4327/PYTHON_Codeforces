import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())

    # l(a0) + k*(k+1)//2 <= r 인 최대 k 찾기
    # = k*(k+1)//2 <= r-l
    diff = r-l
    
    lo, hi = 1, 10**9
    while lo <= hi:
        mid = (lo+hi)//2
        if mid*(mid-1)//2 <= diff:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    print(ans)