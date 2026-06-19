import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if A[i] >= A[j]:
                ans += 1
                
    print(ans)