import sys
input = sys.stdin.readline

s, n = map(int, input().split())

dragons = [tuple(map(int, input().split())) for _ in range(n)]
dragons.sort(key=lambda x: (x[0], -x[1]))

for x, y in dragons:
    if not s>x:
        print('NO')
        break
    else:
        s += y
else:    
    print('YES')