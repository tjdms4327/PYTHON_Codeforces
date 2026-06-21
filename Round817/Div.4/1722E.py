import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    
    grid = [[0]*1001 for _ in range(1001)]
    for _ in range(n):
        h, w = map(int, input().split())
        grid[h][w] += h*w
        
    prefix = [[0]*1001 for _ in range(1001)]
    for h in range(1, 1001):
        for w in range(1, 1001):
            prefix[h][w] = prefix[h-1][w] - prefix[h-1][w-1] + prefix[h][w-1] + grid[h][w]
    
    for _ in range(q):
        hs, ws, hb, wb = map(int, input().split())
        ans = (prefix[hb-1][wb-1]
               - prefix[hs][wb-1]
               - prefix[hb-1][ws]
               + prefix[hs][ws]
        )
        print(ans)