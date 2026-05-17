import sys
input = sys.stdin.readline

mapping = {'p':'q', 'q':'p', 'w':'w'}

t = int(input())
for _ in range(t):
    s = list(input().strip())
    
    b = [mapping[x] for x in s[::-1]]
    print(''.join(b))