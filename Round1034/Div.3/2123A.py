import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    nums = [i%4 for i in range(n)]
    c0, c1, c2, c3 = [nums.count(i) for i in range(4)]
    
    if c0==c3 and c1==c2:
        print('Bob')
    else:
        print('Alice')