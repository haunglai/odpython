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


def transform(numStr, input_str):
    money = 0;
    num = int(numStr);
    if (input_str == 'C'):
        money = num * 100
    elif (input_str == 'J'):
        money = float(num) * 10000 / 1825
    elif (input_str == 'H'):
        money = float(num) * 10000 / 123
    elif (input_str == 'E'):
        money = float(num) * 10000 / 14
    elif (input_str == 'G'):
        money = float(num) * 10000 / 12
    elif (input_str == 'f'):
        money = num * 1;
    elif (input_str == 's'):
        money = float(num) * 100 / 1825
    elif (input_str == 'c'):
        money = float(num) * 100 / 123
    elif (input_str == 'e'):
        money = float(num) * 100 / 14
    elif (input_str == 'p'):
        money = float(num) * 100 / 12

    return money


def exchange(input_str):
    temp = ""
    money = 0.0
    for i in range(len(input_str)):
        c = input_str[i]
        if (c.isdigit()):
            temp += c;
        else:
            if (temp == ""):
                continue

            money += transform(temp, c)
            i += 2  # 因为货币的简写至少为3位，所以可以跳两位
            temp = ""

    return money;


# 处理输入
m = int(input())
money = 0
for i in range(m):
    money += exchange(input())

print(int(money))
