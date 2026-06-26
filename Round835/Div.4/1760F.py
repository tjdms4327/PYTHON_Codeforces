import sys
input = sys.stdin.readline
from math import ceil

t = int(input())
for _ in range(t):
    n, c, d = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    
    A.sort(reverse = True)
    if sum(A[:d]) >= c:
        print('Infinity')
        continue
    
    prefix = [0]
    for x in A:
        prefix.append(prefix[-1] + x)
    
    for k in range(d, -1, -1):
        cycle = k + 1 # k일 쉬고 다음날 하니까 i일에 하면 그 다음은 i+k+1일임.
        temp = d // cycle
        remainder = d % cycle
        
        max_coin =  prefix[min(cycle, n)]
        tot = max_coin*temp + prefix[min(remainder, n)]
        if tot >= c:
            print(k) 
            break
    else:
        print('Impossible')
