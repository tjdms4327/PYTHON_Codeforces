import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

firstwake = input().strip(); m = len(firstwake)
secondwake = input().strip()

res = [False, False]

idx1 = s.find(firstwake)
if idx1 != -1:
    idx2 = s.find(secondwake, idx1+m)
    if idx2 != -1:
        res[0] = True
    
reversed_s = s[::-1]
idx1 = reversed_s.find(firstwake)
if idx1 != -1:
    idx2 = reversed_s.find(secondwake, idx1+m)
    if idx2 != -1:
        res[1] = True
    
    
    
if res[0] == res[1] == True:
    ans = 'both'
elif res[0] == True:
    ans = 'forward'
elif res[1] == True:
    ans = 'backward'
else:
    ans = 'fantasy'
    
print(ans)