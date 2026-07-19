import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    coins = []
    temp = 1
    for _ in range(n):
        temp *= 2
        coins.append(temp)
    coins.sort()
    
    
    one = sum(coins[i] for i in range(n//2-1)) + coins[-1]
    two = sum(coins) - one
    print(abs(one - two))