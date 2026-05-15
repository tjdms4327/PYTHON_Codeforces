import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

tot = 0

zero_cnt = A.count(0)

neg = [a for a in A if a<0]
neg.sort()
for a in neg:
    tot += (-1-a)
if len(neg)%2:
    if zero_cnt:
        tot += 1
        zero_cnt -= 1
    else:
        tot -= (-1-neg[0])
        tot += (1-neg[0])

tot += zero_cnt
    
pos = [a for a in A if a>0]
for a in pos:
    tot += (a-1)
    
print(tot)
