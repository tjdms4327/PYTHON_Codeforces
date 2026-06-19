import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    cand = []

    i = 0
    while i < n:
        j = i
        while j < n and A[j] == A[i]:
            j += 1

        if j - i >= k:
            cand.append(A[i])

        i = j


    # 예외
    if not cand:
        print(-1)
        continue

    # 처리
    l = r = cand[0]
    ans_l = ans_r = cand[0]

    for x in cand[1:]:
        if x == r + 1:
            r = x
        else:
            if r - l > ans_r - ans_l:
                ans_l, ans_r = l, r
            l = r = x

    if r - l > ans_r - ans_l:
        ans_l, ans_r = l, r

    print(ans_l, ans_r)