import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    even, odd = [], []
    for a in sorted(A):
        if a%2:
            odd.append(a)
        else:
            even.append(a)
            
    mihai = sum(even)
    bianca = sum(odd)
    if mihai > bianca:
        print('YES')
    else:
        print('NO')    