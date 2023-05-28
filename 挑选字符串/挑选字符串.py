# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 处理输入
a = input()
b = input()
count = 0

while (True):
    last = 0
    flag = False
    # 逐个在字符串A中找字符串B的每一个字符,如果找到了，按照规则，这个字符就不能再用，可以直接置一个无效字符。
    for single_char in b:
        # A中出现位置
        index = a.find(str(single_char), last)
        last = index
        if (index != -1):
            a = a.replace(single_char, '_', 1)
        else:
            flag = True
            break
    if (flag):
        break

    count += 1
print(count)




