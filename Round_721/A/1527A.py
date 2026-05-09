import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    k = 1 << (n.bit_length()-1)
    print(k-1)