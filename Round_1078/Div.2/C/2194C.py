import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    S = [input().strip() for _ in range(k)]
    
    position = [list(col) for col in zip(*S)]
    
    pos_mask = []
    for i in range(n):
        mask = 0
        for c in position[i]:
            mask |= 1 << (ord(c)-97)
        pos_mask.append(mask)
        
    divs = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            divs.append(d)
            if d * d != n:
                divs.append(n//d)
    divs.sort()
    
    answer_d = n
    answer_pattern = None
    for d in divs: # 패턴 찾기 시작
        ok = True
        pattern = [0]*d
        for i in range(d):
            cur = pos_mask[i]
            j = i + d
            while j < n:
                cur &= pos_mask[j]
                if cur == 0: # 이 d는 불가능
                    ok = False
                    break
                j += d
            if not ok: # 한 그룹 실패하면 다음 d로 넘어감
                break
            pattern[i] = cur # 성공한 그룹 저장
        if ok:
            answer_d = d
            answer_pattern = pattern
            break
 
    res = []
    for i in range(answer_d):
        mask = answer_pattern[i]
        c = (mask & -mask).bit_length() - 1
        res.append(chr(c + 97))
 
    res = ''.join(res) * (n // answer_d)
    print(res)
