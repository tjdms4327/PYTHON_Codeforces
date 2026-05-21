import sys
input = sys.stdin.readline

k, r = map(int, input().split())

price = k
while True:
    if price%10==0:
        break
    elif (price-r)%10 == 0:
        break
    else:
        price += k

print(price//k)
