import sys
input = sys.stdin.readline

a, b = map(int, input().split())

diff_pair = min(a, b)
same_pair = (max(a, b) - diff_pair)//2

print(diff_pair, same_pair)
