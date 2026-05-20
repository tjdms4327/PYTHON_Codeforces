import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))

for i in range(len(n)):
    if i==0 and n[i]==9:
        continue
    if n[i] > 9-n[i]:
        n[i] = 9-n[i]
        
print(''.join(str(x) for x in n))