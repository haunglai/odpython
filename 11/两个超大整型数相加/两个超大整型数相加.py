while 1:
    try:
        a = input()
        b = input()

        max_lens = max(len(a), len(b))

        a = a.zfill(max_lens)
        b = b.zfill(max_lens)

        ret = ""
        dp = 0

        while max_lens > 0:
            max_lens -= 1
            temp = int(a[max_lens]) + int(b[max_lens]) + dp
            if temp >= 10:
                dp = 1
                ret += str(temp % 10)
            else:
                dp = 0
                ret += str(temp)
        if dp == 1:
            print("1" + ret[::-1])
        else:
            print(ret[::-1])
    except Exception:
        break
