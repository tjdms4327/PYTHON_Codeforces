import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))

l, r = 0, n-1
alice_time = 0
bob_time = 0

while l <= r:
    if alice_time <= bob_time:
        alice_time += time[l]
        l += 1
    else:
        bob_time += time[r]
        r -= 1
        
print(l, n-l)
        