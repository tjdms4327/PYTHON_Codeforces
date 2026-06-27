import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    A = list(map(int, input().split()))
    
    
    need = [i+1+A[i] for i in range(n)]
    need.sort()
    
    prefix = [0]*n
    prefix[0] = need[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + need[i]
        
    for i in range(n):
        if prefix[i] > c:
            print(i)
            break
    else:
        print(n)