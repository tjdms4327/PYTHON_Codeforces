import sys, math
input = sys.stdin.readline

MAX = 10**6
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, MAX+1, i):
            is_prime[j] = False

n = int(input())
X = list(map(int, input().split()))

for x in X:
    r = math.isqrt(x)
    if r**2 == x and is_prime[r]:
        print('YES')
    else:
        print('NO')