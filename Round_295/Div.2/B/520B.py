import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

MAX = 10**5+1
dist = [-1] * MAX
dist[n] = 0

queue = deque([n])
while queue:
    cur = queue.popleft()
    if cur == m:
        print(dist[cur])
        break
    
    for nxt in (cur*2, cur-1):
        if 0<= nxt <= MAX and dist[nxt]==-1:
            dist[nxt] = dist[cur]+1
            queue.append(nxt)