import sys, math
input = sys.stdin.readline

y, w = map(int, input().split())

win = 6 - max(y, w) + 1

GCD = math.gcd(win, 6)
print(f'{win//GCD}/{6//GCD}')