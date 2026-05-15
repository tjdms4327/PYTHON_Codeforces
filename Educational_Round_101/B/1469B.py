import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    R = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    
    prefix_R = [0]*n
    prefix_R[0] = R[0]
    for i in range(1, n):
        prefix_R[i] = prefix_R[i-1] + R[i]
    prefix_R += [0]
    
    prefix_B = [0]*m
    prefix_B[0] = B[0]
    for i in range(1, m):
        prefix_B[i] = prefix_B[i-1] + B[i]
    prefix_B += [0]
        
    print(max(prefix_B) + max(prefix_R))