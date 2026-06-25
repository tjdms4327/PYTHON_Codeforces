import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    compressed = [A[0]]
    for a in A[1:]: 
        if a != compressed[-1]: compressed.append(a)
    m = len(compressed)
    
    cnt = 0
    for i in range(m):
        left = (i == 0 or compressed[i] < compressed[i-1])
        right = (i == m-1 or compressed[i] < compressed[i+1])

        if left and right:
            cnt += 1
    
    if cnt == 1:
        print('YES')
    else:
        print('NO')
    
            