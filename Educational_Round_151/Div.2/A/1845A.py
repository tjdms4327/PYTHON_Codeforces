import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())

    if x != 1:
        print("YES")
        print(n)
        print(*([1] * n))

    else:
        if n % 2 == 0:
            if k < 2:
                print('NO')
            else:
                print("YES")
                print(n // 2)
                print(*([2] * (n // 2)))

        else:
            if k < 3:
                print("NO")
            else:
                print("YES")
                arr = [3] + [2] * ((n - 3) // 2)
                print(len(arr))
                print(*arr)