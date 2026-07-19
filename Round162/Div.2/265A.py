import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

liss = 0
for x in t:
    if x == s[liss]:
        liss += 1
        
print(1+liss) # 1-based