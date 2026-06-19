import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s = map(int, input().strip().split())
    A = list(map(int, input().split()))
    
    Sum = sum(A)
    if s > Sum:
        print(-1)
        continue
    elif s == Sum:
        print(0)
        continue
    
    left = 0
    cur = 0
    mx = -1
    for right in range(n):
        cur += A[right]
        
        while cur > s:
            cur -= A[left]
            left += 1
        
        if cur == s:
            mx = max(mx, right-left+1)
            
    print(n-mx)