import sys
input = sys.stdin.readline

standard = input().strip()
hands = list(input().strip().split())

for x in hands:
    if x[0]==standard[0] or x[1]==standard[1]:
        print('YES')
        break
else:
    print('NO')
