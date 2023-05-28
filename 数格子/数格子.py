
while 1:
    try:
        n = int(input())

        lst = []
        for _ in range(n):
            lst.append(list(map(int, input().split())))

        x, y = list(map(int, input().split()))

        count = 0
        for i in range(x - 1, x + 1 + 1):
            for j in range(y - 1, y + 1 + 1):
                # 中心点
                if i == x and j == y:
                    pass
                elif 0 <= i < len(lst) and 0 <= j < len(lst[0]):
                    count += lst[i][j]
        print(count)
    except Exception:
        break
