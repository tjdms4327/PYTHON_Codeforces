import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    X, Y = set(), set()
    for _ in range(4):
        x, y = map(int, input().split())
        X.add(x)
        Y.add(y)
        
    x_len = max(X) - min(X)
    y_len = max(Y) - min(Y)
    print(x_len*y_len)    