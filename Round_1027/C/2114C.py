import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    
    cnt = 0
    prev = -1
    for a in A:
        if a > prev+1:
            cnt += 1
            prev = a
            
    print(cnt)