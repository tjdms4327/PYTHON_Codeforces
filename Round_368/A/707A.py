import sys
input = sys.stdin.readline

n, m = map(int, input().split())
picture = [list(input().strip().split()) for _ in range(n)]

for row in picture:
    if set(row) <= {'W', 'G', 'B'}:
        continue
    else:
        print('#Color')
        break
else:
    print('#Black&White')