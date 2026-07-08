import sys
input = sys.stdin.readline

keypad = [list(input().strip()) for _ in range(3)]

keypad180 = [row[::-1] for row in keypad[::-1]]

if keypad == keypad180:
    print('YES')
else:
    print('NO')