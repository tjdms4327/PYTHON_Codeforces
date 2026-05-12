import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    S.sort()
    
    diff = 1001
    for i in range(1, n):
        diff = min(diff, S[i]-S[i-1])
        
    print(diff)