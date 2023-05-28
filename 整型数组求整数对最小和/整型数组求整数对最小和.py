while 1:
    try:
        lst1 = list(map(int, input().split()))[1:]
        lst2 = list(map(int, input().split()))[1:]
        k = int(input())

        dp = []
        for i in lst1:
            for j in lst2:
                dp.append(i+j)

        dp = sorted(dp)
        print(sum(dp[:k]))
    except Exception:
        break
