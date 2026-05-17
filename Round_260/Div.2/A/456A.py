import sys
input = sys.stdin.readline

laptops = []

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    laptops.append((a, b))
laptops.sort()
    
    
for i in range(1, n):
    if laptops[i-1][0]<laptops[i][0]\
        and laptops[i-1][1]>laptops[i][1]:
            print('Happy Alex')
            break
else:
    print('Poor Alex')