import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int, input().split()))
    
    A = [B[0]]
    for i in range(1, n):
        if B[i-1] <= B[i]:
            A.append(B[i])
        else:
            A.extend([1, B[i]])
            
    print(len(A))
    print(*A)