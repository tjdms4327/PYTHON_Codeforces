import sys
input = sys.stdin.readline

lucky = [4, 44, 47, 444, 447, 474, 477,
         7, 74, 77, 777, 774, 747, 744]
lucky.sort()

n = int(input())
for x in lucky:
    if n % x == 0:
        print('YES')
        sys.exit()
else:
    print('NO')
