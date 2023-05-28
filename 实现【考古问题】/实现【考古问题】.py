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


def fac(strs, lis, result):
    for i in range(len(lis)):
        str_i = strs + lis[i]
        lis_i = lis[0:i] + lis[(i + 1):]
        if not lis_i:
            if str_i not in result:
                result.append(str_i)
        else:
            fac(str_i, lis_i, result)


result = []
num = int(input())
list_n = input().split(' ')
fac('', list_n, result)
result.sort()
for s in result:
    print(s)