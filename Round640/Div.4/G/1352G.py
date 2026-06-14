import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
     
    if n in [2, 3]:
        print(-1)
        continue
    
    left = [x for x in range(1, n+1,2)][::-1]
    right = [x for x in range(2, n+1, 2)]
    right[:2] = right[:2][::-1]
    
    print(*(left+right))
