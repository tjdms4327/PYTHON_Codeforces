import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pref1 = [0] * (n+1)
    pref3 = [0] * (n+1)
    for i in range(n):
        pref1[i+1] = pref1[i] + (a[i] == 1)
        pref3[i+1] = pref3[i] + (a[i] == 3)

    ok = False
    for i in range(1, n-1):
        # [0:i]
        if pref1[i] * 2 < i:
            continue

        for j in range(i+1, n):
            # [i:j]
            cnt3 = pref3[j] - pref3[i]
            length = j - i

            if cnt3 * 2 <= length:
                ok = True
                break

        if ok:
            break

    print("YES" if ok else "NO")