import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
start = 1
ans = 0

def dfs(cur, parent, cat_cnt):
    global ans
    
    if A[cur] == 1:
        cat_cnt += 1
    else:
        cat_cnt = 0
        
    if cat_cnt > m:
        return
    
    is_leaf = True
    for nxt in graph[cur]:
        if nxt != parent: # 다시 올라가는 것 막기
            is_leaf = False
            dfs(nxt, cur, cat_cnt)
    
    if is_leaf:
        ans += 1
        
dfs(start, start, 0)
print(ans)