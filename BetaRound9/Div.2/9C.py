import sys
input = sys.stdin.readline

n = int(input())

def dfs(x):
    if x > n:
        return 0
    
    return 1 + dfs(x*10) + dfs(x*10+1)

print(dfs(1))