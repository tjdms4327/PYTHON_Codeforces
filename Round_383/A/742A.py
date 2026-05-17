import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(1)
    sys.exit()
    
repeat = [8, 4, 2, 6]
n %= 4
print(repeat[n-1])
