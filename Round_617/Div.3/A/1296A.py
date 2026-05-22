import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    odd_cnt = sum(1 for a in A if a%2)
    if odd_cnt == 0:
        print('NO')
    elif odd_cnt == n and n%2==0:
        print('NO')
    else:
        print('YES')
     