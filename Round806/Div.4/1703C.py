import sys
input = sys.stdin.readline

mapping_org = {'U':-1, 'D':1}

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    res = [0] * n
    for i in range(n):
        m, lst = input().strip().split()
        B = [mapping_org[b] for b in list(lst)]
        move = sum(B)
        
        res[i] = (A[i]+move)%10
        
    print(*res)