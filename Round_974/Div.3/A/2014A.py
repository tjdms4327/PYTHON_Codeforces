import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    robin = [0,0]
    for a in A:
        if a >= k:
            robin[1] += a
        elif a == 0 and robin[1]>0:
            robin[0] += 1
            robin[1] -= 1
            
    print(robin[0])
