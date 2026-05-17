import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    odd = sum(1 for a in A if a%2)
    if odd == n:
        print('YES')
    else:
        print('NO')    