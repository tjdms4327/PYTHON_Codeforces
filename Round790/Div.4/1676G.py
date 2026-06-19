import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    s = input().strip()
    
    ### 트리 구현
    tree = [[] for _ in range(n+1)]
    for child in range(2, n+1):
        parent = A[child-2]
        tree[parent].append(child)
    
    ### DFS 구현
    ans = [0]
    def dfs(u):
        cur = 1 if s[u-1]=='W' else -1
        
        for child in tree[u]:
            cur += dfs(child)
            
        if cur == 0:
            ans[0] += 1
        
        return cur
    
    dfs(1)
    print(ans[0])