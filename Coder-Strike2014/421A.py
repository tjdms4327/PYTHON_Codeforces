import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
arthur_like = list(map(int, input().split()))
alexander_like = list(map(int, input().split()))

ans = []
for i in range(1, n+1):
    if i in arthur_like:
        ans.append(1)
    elif i in alexander_like:
        ans.append(2)
        
print(*ans)
