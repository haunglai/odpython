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


def comp(a, b):
    return b[1] - a[1]


# 处理输入
input_str = input()

n = len(input_str)
stack = []
flag = False
valid_flag = False

for i in range(n):
    if (input_str[i] == 'M'):
        # 无效判断
        # 1:中间无效
        if (i - 1 >= 0 and input_str[i - 1] == 'M' and i + 1 < n and input_str[i + 1] == 'M'):
            print(-1)
            valid_flag = True
            break

        # 2:两边无效
        if ((i - 1 == 0 and input_str[i - 1] == 'M') or (i + 1 == n and input_str[i - 1] == 'M')):
            print(-1)
            valid_flag = True
            break

        # 当前机柜的左右位置
        pos_left = max(0, i - 1)
        pos_right = min(n - 1, i + 1)

        if (len(stack) > 0 and not flag):
            # 满足 MIM 的样式
            if (stack[-1] == pos_left):
                stack.pop()
                flag = True
        else:
            flag = False

        stack.append(pos_right)

if not valid_flag:
    print(len(stack))