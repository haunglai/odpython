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

num = int(input())
array = []


def a(s):
    count = 0
    t = re.findall('(\d+)(M|G|T)', s)
    if len(t) > 0:
        for v in t:
            if v[1] == 'M':
                count = int(v[0]) + count
            elif v[1] == 'G':
                count = int(v[0]) * 1024 + count
            elif v[1] == 'T':
                count = count + int(v[0]) * 1024 * 1024
        return count
    else:
        return 0


for i in range(num):
    h = input()
    array.append((a(h), h))

array = sorted(array, key=lambda x: x[0])

for i in array:
    print(i[1])