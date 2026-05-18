import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

seen = set()
dict = {}
for i in range(n-1):
    slice = s[i:i+2]
    if slice in seen:
        dict[slice] += 1
    else:
        seen.add(slice)
        dict[slice] = 1
    
sorted_d = sorted(dict.items(), key=lambda x: -x[1])
print(sorted_d[0][0])