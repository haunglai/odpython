while 1:
    try:
        n = int(input())

        temp = []
        for _ in range(n):
            temp += list(map(int, input().split()))

        total = sum(temp)
        print(total)
    except Exception:
        break
