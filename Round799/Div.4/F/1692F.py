import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    temp = Counter([x%10 for x in A])
    
    cand = []
    for key, val in temp.items():
        count = min(3, val)
        cand.extend([key]*count)
        
    length = len(cand)
        
    found = False
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if (cand[i]+cand[j]+cand[k])%10 == 3:
                    found = True
                    break
            if found:
                break
        if found:
            break

    print("YES" if found else "NO")