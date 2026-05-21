import sys
input = sys.stdin.readline

X = list(map(int, input().split()))

Sum  = max(X)

abc = [Sum-x for x in X if Sum!=x]
print(*abc)
