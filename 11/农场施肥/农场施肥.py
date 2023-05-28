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


def cal(k, fields):
    days = 0
    for i in range(len(fields)):
        days += math.ceil(fields[i] / float(k))
    return days


# 处理输入
params = [int(x) for x in input().split(" ")]
m = params[0]
n = params[1]
fields = [int(x) for x in input().split(" ")]

# 最少天数小于果林大小可直接返回-1
if (n < len(fields)):
    print(-1)
else:
    # 排序找到最小值
    fields = sorted(fields)
    left = fields[0]
    right = fields[len(fields) - 1]

    result = -1
    while (left + 1 < right):
        # 取中间位置的值作为效能k，
        k = int(math.ceil(float(left + right) / 2))

        res = cal(k, fields)

        if (res - n > 0):
            left = k
        else:
            result = k
            right = k
    print(result)
