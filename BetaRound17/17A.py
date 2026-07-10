import sys
input = sys.stdin.readline

n, k = map(int, input().split())

is_prime = [True]*(n+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for x in range(i*i, n+1, i):
            is_prime[x] = False
            
primes = [i for i in range(2, n+1) if is_prime[i]]
m = len(primes)

cnt = 0
for i in range(1, m):
    x = primes[i] + primes[i-1] + 1 
    if x <= n and is_prime[x]:
        cnt += 1
    
    if cnt >= k:
        break
    
if cnt < k:
    print('NO')
else:
    print('YES')