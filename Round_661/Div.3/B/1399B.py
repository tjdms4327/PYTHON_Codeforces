import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    minA, minB = min(A), min(B)
    
    cnt = 0
    for a, b in zip(A, B):
        diffA = a - minA
        diffB = b - minB
        
        temp = min(diffA, diffB)
        cnt += temp + (diffA-temp) + (diffB-temp)
        
    print(cnt)