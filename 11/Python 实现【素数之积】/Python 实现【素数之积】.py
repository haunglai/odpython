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


def factor(num):
    if num == 1:
        return []
    else:
        for i in range(2, num + 1):
            a, b = divmod(num, i)
            if b == 0:
                return [i] + factor(a)


num = int(input())
if num > 2147483646:
    print('-1 -1')
list_out = factor(num)
if len(list_out) == 2:
    print('{} {}'.format(list_out[0], list_out[1]))
else:
    print('-1 -1')