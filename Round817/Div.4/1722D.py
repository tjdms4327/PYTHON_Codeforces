import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    directions = input().strip()
    
    score = 0
    diff = [0]*n
    for idx, d in enumerate(directions):
        if d == 'L':
            score += idx
            diff[idx] = n-1 - 2*idx
        else:
            score += n-1-idx
            diff[idx] = idx - (n-1-idx)
    diff.sort(reverse=True)
    
    
    cur, best = 0, 0
    res = []
    for i in range(n):
        cur += diff[i]
        best = max(best, cur)
        res.append(score + best)
    
    print(*res)