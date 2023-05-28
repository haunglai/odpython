m, t, p = list(map(int, input().split()))
s_list = list(map(int, input().split()))
items = [0 for _ in range(len(s_list))]
for i in range(len(s_list)):
    if s_list[i] <= 0:
        items[i] = 0
    elif i > 0 and ((s_list[i] - s_list[i - 1] >= 10) or s_list[i] < s_list[i - 1]):
        items[i] = 0
    else:
        items[i] = 1
i = 0

while i < len(s_list):
    if items[i] == 0 and i > 0 and items[i - 1] == 1:
        s_list[i], items[i] = s_list[i - 1], 1
    error_num, corrent, j = 0, 0, i
    while m > 0 and j < len(s_list):
        if items[j] == 0:
            error_num += 1
            if error_num >= t:
                corrent = j - 1 if j > 0 else 0
        j += 1
    if error_num >= t:
        pos, k = False, 0
        while k < i and items[k] != 1:
            k += 1
        else:
            pos = True
        if i + t == len(s_list) - 1:
            k = i
            while k < corrent + 1:
                s_list[k], items[k] = s_list[i - 1], 1
                k += 1
            break
        elif i + m <= len(s_list):
            for k in range(i, len(s_list)):
                if k < corrent + 1:
                    s_list[k] = s_list[i - 1] if i > 0 else s_list[0]
                    items[k] = 1
                else:
                    items[k] = 0
        else:
            for k in range(i, i + m):
                if k < corrent + 1:
                    s_list[k] = s_list[i - 1]
                    items[k] = 1
                else:
                    items[k] = 0
            if i + m + p >= len(s_list) + 1:
                for k in range(i, len(s_list)):
                    items[k] = 0
                else:
                    items[k], i = 0, k + p
    else:
        i += 1
res, location = 0, 0
for item in range(len(items)):
    if items[item] != 1:
        if location > res:
            res = location
        location = 0
    else:
        location += 1
print(max(res, location))