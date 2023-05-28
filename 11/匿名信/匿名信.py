# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools

# 输入加排序一并做了
newspaper = [''.join(sorted(x)) for x in input().split(" ")]
anonymousLetter = [''.join(sorted(x)) for x in input().split(" ")]

flag = False
for letter in anonymousLetter:
    if letter not in newspaper:
        flag = True
        break

if flag:
    print(False)
else:
    print(True)