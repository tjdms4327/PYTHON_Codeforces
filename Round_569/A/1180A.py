import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(1)
    sys.exit()
    
tot = 0
for i in range(1, 2*n, 2):
    tot += 2*i
tot -= 2*n-1

print(tot)