# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools


# 字符串去重后个数
def distinct_length(s):
    str_set = set()
    for c in s:
        str_set.add(c)
    return len(str_set)


# 处理输入
string1 = input()
string2 = input()

temp = ""
res_list = []
max_length = 0;
diffLen = distinct_length(string2);
for i in range(len(string1)):
    c = string1[i]
    # 有效字母
    if (c >= 'g' and c <= 'z'):
        temp += c
        if (i != len(string1) - 1):
            continue

    if (temp != ""):
        temp_len = distinct_length(temp)
        # 数量必须要小于等于string2的不同字母数量
        if (temp_len <= diffLen):
            if (temp_len > max_length):
                res_list = []
                max_length = max(max_length, temp_len)

            res_list.append(temp);
        temp = ""

res_list = sorted(res_list)
if len(res_list) == 0:
    print("Not Found")
else:
    print(res_list[len(res_list) - 1])

