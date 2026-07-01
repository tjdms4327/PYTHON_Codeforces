import sys
input = sys.stdin.readline

lines = list(map(int, input().split()))
lines.sort()

cand = [(0,1,2), (0,1,3), (0,2,3),
        (1,2,3)]

ans = 'IMPOSSIBLE'
for i, j, k in cand:
    a, b, c = lines[i], lines[j], lines[k]
    if a + b > c:
        ans = 'TRIANGLE'
        break
    elif a + b == c and ans != 'TRIANGLE':
        ans = 'SEGMENT'

    
print(ans) 