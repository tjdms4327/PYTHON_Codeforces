import sys
input = sys.stdin.readline

d, sumTime = map(int, input().split())

ans = []
maxdiff = []
for _ in range(d):
    minTime, maxTime = map(int, input().split())
    ans.append(minTime)
    maxdiff.append(maxTime - minTime)

minSum = sum(ans)
if (sumTime < minSum) or (sumTime > minSum+sum(maxdiff)):
    print('NO')
elif sumTime == minSum:
    print('YES')
    print(*ans)
else:
    needed = sumTime - minSum
    for i in range(d):
        adding = maxdiff[i]
        
        if adding >= needed:
            ans[i] += needed
            break
        else:
            ans [i] += adding
            needed -= adding
    
    print('YES')
    print(*ans)