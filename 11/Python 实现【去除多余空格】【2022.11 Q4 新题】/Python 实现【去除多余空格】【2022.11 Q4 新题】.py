while 1:
    try:
        n = int(input())
        for _ in range(n):
            line = input()
            # 从 0 开始，步长为 8 到 len(line) 结束
            for i in range(0, len(line), 8):
                if len(line[i: i+8]) == 8:
                    print(line[i: i+8])
                else:
                	# 右侧补0
                    print(line[i: i+8].ljust(8, "0"))
    except Exception as e:
        break
