# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import sys
from collections import Counter, defaultdict
import copy
from itertools import permutations
import re
import math
import sys

input_str = input()

res = "";
temp = "";
for i in range(len(input_str)):
    c = str(input_str[i])
    # 是否为字母
    if (c.isalpha()):
        temp += c;
    # 遇到空格，对上一个字符串进行翻转
    elif (c == " "):
        res += temp[::-1] + " "
        temp = ""
        # 遇到标点符号，对上一个字符串进行翻转，并加上当前字符
    else:
        if (temp != ""):
            res += temp[::-1]
            temp = ""
        res += c
    if (i == len(input_str) - 1 and temp != ""):
        res += temp[::-1]

print(res)
