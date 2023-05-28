

signals = input()
if "010" not in signals:
    print(-1)
sign = "010"
for i in range(len(signals)):
    if sign + "11" in signals and sign + "10" not in signals:
        print(sign)
        break
    else:
        if sign in signals:
            sign += "10"
        else:
            print(sign[:-2])
            break