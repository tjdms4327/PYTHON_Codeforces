import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

ans = 0
for i in range(n):
    if s[i] == 'A':
        left = s[:i].count('Q')
        right = s[i+1:].count('Q')
        ans += left*right
        
print(ans)
