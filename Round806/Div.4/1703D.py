import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    S = [input().strip() for _ in range(n)]
    st = set(S)

    ans = ['0'] * n

    for idx, s in enumerate(S):
        L = len(s)
        pref = ""

        for i in range(L - 1):
            pref += s[i]
            suff = s[i+1:]

            if pref in st and suff in st:
                ans[idx] = '1'
                break

    print(''.join(ans))