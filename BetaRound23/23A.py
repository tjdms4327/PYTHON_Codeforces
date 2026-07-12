import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

for i in range(n-1, 0, -1):
    seen = set()
    for l in range(n-i+1):
        slice = s[l:l+i]
        if slice in seen:
            print(i)
            sys.exit()
        seen.add(slice)
            
print(0)