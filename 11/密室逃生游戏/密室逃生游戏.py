# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

key = input()
boxes = [x for x in input()[2:].split(" ")]

res = -1
for i in range(len(boxes)):
    # 先全部转为小写字母
    lower = boxes[i].lower()
    char_set = set([])
    for c in lower:
        if (c >= 'a' and c <= 'z'):
            char_set.add(c)

    if (len(char_set) == len(key)):
        if (key == "".join(char_set)):
            res = i + 1
            break

print(res)