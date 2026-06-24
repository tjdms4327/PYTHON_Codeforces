import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    odd = [1 if x%2 else 0 for x in A]
    
    cnt = 0
    for i in range(1, n):
        if odd[i]==odd[i-1]:
            cnt += 1
            
    print(cnt)
    