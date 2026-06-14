import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    if n < k:
        print('NO')
        continue
    
    if n%2:
        if k%2:
            ans = [1]*(k-1) + [n-k+1]
            print('YES')
            print(*ans)
        else:
            print('NO')
    else: # 짝수
        if k%2==0:
            ans = [1]*(k-1) + [n-k+1]
            print('YES')
            print(*ans)
        elif n >= 2*k:
            ans = [2]*(k-1) + [n-2*(k-1)]
            print('YES')
            print(*ans)
        else:
            print('NO')
