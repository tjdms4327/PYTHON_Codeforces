import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    matrix = [list(input().strip()) for _ in range(8)]
    
    cand = [(idx, row) for idx, row in enumerate(matrix) if row.count('#')==1]
    
    ans = (-1,-1)
    for idx, row in cand:
        col_idx = row.index('#')
        if 0<idx<7:
            if matrix[idx-1] == matrix[idx+1]:
                ans = (idx+1, col_idx+1)
                break
        elif idx == 0:
            if matrix[idx+1][col_idx-1:col_idx+2] == '#.#':
                ans = (idx+1, col_idx+1)
                break
        elif idx == 7:
            if matrix[idx-1][col_idx-1:col_idx+2] == '#.#':
                ans = (idx+1, col_idx+1)
                break
    
    print(*ans)
