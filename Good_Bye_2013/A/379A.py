import sys
input = sys.stdin.readline

a, b = map(int, input().split())

tot = a
while a >= b:
    temp = a//b
    tot += temp
    a = temp + a%b

print(tot)
    
