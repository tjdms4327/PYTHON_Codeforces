import sys
input = sys.stdin.readline

s = input().strip()

tot = min(ord(s[0])-ord('a'), (26 - ord(s[0]) + ord('a')))
for i in range(1, len(s)):
    dist = abs(ord(s[i]) - ord(s[i-1]))
    tot += min(dist, 26-dist)
    
print(tot)