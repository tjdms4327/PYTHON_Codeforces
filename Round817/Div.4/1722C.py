import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = set(input().split())
    B = set(input().split())
    C = set(input().split())
     
    all_words = A | B | C
    
    score = [0, 0, 0]
    for w in A | B | C:
        cnt = (w in A) + (w in B) + (w in C)
        if cnt == 1:
            if w in A: 
                score[0] += 3
            elif w in B: 
                score[1] += 3
            else: 
                score[2] += 3
        elif cnt == 2:
            if w not in A: 
                score[1] += 1; score[2] += 1
            elif w not in B: 
                score[0] += 1; score[2] += 1
            else: 
                score[0] += 1; score[1] += 1
    
    print(*score)