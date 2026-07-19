import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    matrix = [list(input().strip()) for _ in range(10)]
    
    tot = 0
    for r in range(10):
        for c in range(10):
            if (matrix[r][c] == 'X'):
                if (r in [0, 9] and 0<=c<=9) or (0<=r<=9 and c in [0, 9]):
                    tot += 1
                elif (r in [1, 8] and 1<=c<=8) or (1<=r<=8 and c in [1, 8]):
                    tot += 2
                elif (r in [2, 7] and 2<=c<=7) or (2<=r<=7 and c in [2, 7]):
                    tot += 3
                elif (r in [3, 6] and 3<=c<=6) or (3<=r<=6 and c in [3, 6]):
                    tot += 4
                else:
                    tot += 5
    print(tot)