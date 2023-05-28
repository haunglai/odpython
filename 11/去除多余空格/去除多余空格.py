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


def check(start, input_str):
    str1 = input_str[0:start]
    count = 0
    # 判断左侧是否有奇数个单引号出现
    for i in range(len(str1)):
        if (str1[i] == '\''):
            count += 1
    if count % 2 == 0:
        return False
    else:
        return True


def get_left_space_count(index, input_str):
    count = 0
    if (index == 0):
        return count
    else:
        while (True):
            index -= 1
            if (index >= 0 and input_str[index] == ' '):
                count += 1
            else:
                break
    if count > 1:
        return count - 1
    else:
        return 0


def get_right_space_count(index, input_str):
    count = 0
    if (index == 0):
        return count
    else:
        while (True):
            index += 1
            if (index < len(input_str) and input_str[index] == ' '):
                count += 1
            else:
                break

    if count > 1:
        return count - 1
    else:
        return 0


# 处理输入
input_str = input()
keywords = input().split(",")

coords = []
count = 0;  # 空格个数

for keyword in keywords:
    keyword_coord = keyword.split(" ")
    start = int(keyword_coord[0])
    end = int(keyword_coord[1])
    left_space_count = 0
    right_space_count = 0
    coord = []
    if (not check(start, input_str)):
        left_space_count = get_left_space_count(start, input_str)
        right_space_count = get_right_space_count(end, input_str)

    coord.append(start - count - left_space_count)
    coord.append(end - count - left_space_count)
    count += left_space_count + right_space_count  # 记录总共去除的空格数
    coords.append(coord)

res = "";
for coord in coords:
    res += str(coord[0]) + " " + str(coord[1]) + ","

print(res[0:-1])