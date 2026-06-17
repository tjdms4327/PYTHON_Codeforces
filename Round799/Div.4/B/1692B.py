import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    len_set = len(set(A))
    if (n-len_set)%2:
        len_set -= 1
        
    print(len_set)