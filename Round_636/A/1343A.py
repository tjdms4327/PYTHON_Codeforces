import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    tot = 1 + 2
    temp = 2
    while n % tot:
        temp *= 2
        tot += temp
        
    print(n//tot)