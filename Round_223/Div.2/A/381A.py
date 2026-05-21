import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

left, right = 0, n-1

def select_card():
    global left, right
    
    if cards[left] > cards[right]:
        cand = cards[left]
        left += 1
    else:
        cand = cards[right]
        right -= 1
    return cand


sereja,  dima = 0, 0
for i in range(n):
    if i % 2 == 0:
        sereja += select_card()
    else:
        dima += select_card()
        
print(sereja, dima)
