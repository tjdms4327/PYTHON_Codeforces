import sys
input = sys.stdin.readline

patterns = [
    [(0,0),(0,1),(1,0)],
    [(0,0),(0,1),(1,1)],
    [(0,0),(1,0),(1,1)],
    [(0,0),(1,0),(1,-1)]
]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    g = [list(input().strip()) for _ in range(n)]

    visited = [[False]*m for _ in range(n)]
    ok = True

    for i in range(n):
        for j in range(m):
            if g[i][j] != '*' or visited[i][j]:
                continue

            found = False

            for p in patterns:
                cells = []
                valid = True

                for dx, dy in p:
                    ni, nj = i+dx, j+dy

                    if ni<0 or nj<0 or ni>=n or nj>=m:
                        valid = False
                        break
                    if g[ni][nj] != '*':
                        valid = False
                        break

                    cells.append((ni,nj))

                if valid:
                    for x,y in cells:
                        visited[x][y] = True
                    found = True
                    break

            if not found:
                ok = False
                break

        if not ok:
            break

    # adjacency check
    if ok:
        for i in range(n):
            for j in range(m):
                if g[i][j] == '*':
                    cnt = 0
                    for di in [-1,0,1]:
                        for dj in [-1,0,1]:
                            ni, nj = i+di, j+dj
                            if 0<=ni<n and 0<=nj<m and g[ni][nj]=='*':
                                cnt += 1
                    if cnt != 3:
                        ok = False
                        break
            if not ok:
                break

    print("YES" if ok else "NO")